# CRITICAL ISSUE: Metrics Lost on Server Restart

**Date**: 2025-10-19
**Severity**: HIGH
**Status**: UNRESOLVED

## Problem

The fraud simulation server stores all run metrics **IN MEMORY ONLY**. When the server restarts, all metrics counters reset to zero, even though the actual run data still exists on disk.

## What Happened

1. Executed 10 card_testing simulation runs successfully
2. All runs saved to disk in `output/runs/run_card_testing_*/`
3. Restarted fraud sim server to load new fraud types
4. **ALL METRICS RESET TO ZERO**
5. Executed 3 new fraud type runs (velocity_attack, account_takeover, synthetic_identity)
6. Dashboard now shows `runs_total: 3` instead of `runs_total: 13`

## Evidence

```bash
# On disk: 13 run directories exist
$ ls output/runs/ | wc -l
13

# In memory: Only 3 runs tracked
$ curl http://localhost:8082/sim/status
{
  "runs_total": 3.0,
  "runs_completed": 3.0,
  "available_runs": 13
}
```

## Root Cause

**File**: `app/fraud_sim_api.py`
**Class**: `FraudSimMetrics`
**Line**: 20-35

```python
class FraudSimMetrics:
    """Thread-safe metrics for fraud simulation runs"""
    def __init__(self):
        self._lock = threading.Lock()
        self._metrics = {
            'runs_total': 0,           # ← RESETS TO 0 ON RESTART
            'runs_in_progress': 0,
            'runs_completed': 0,       # ← RESETS TO 0 ON RESTART
            'runs_failed': 0,
            'last_run_accuracy': 0.0,
            'last_run_precision': 0.0,
            'last_run_recall': 0.0,
            'last_run_f1_score': 0.0,
            'total_transactions_analyzed': 0,  # ← RESETS TO 0 ON RESTART
            'total_fraud_detected': 0,         # ← RESETS TO 0 ON RESTART
            'pattern_flags': {}
        }
        self._run_history = []  # ← EMPTY ON RESTART
```

**The server NEVER loads existing runs from disk into memory on startup.**

## Impact

- **Grafana dashboards show incorrect data** after any server restart
- **Time-series graphs are broken** - missing historical data points
- **Run comparisons are incomplete** - only shows runs since last restart
- **Metrics are unreliable** - don't reflect actual system usage
- **Data integrity compromised** - counters don't match reality

## What Should Happen

On server startup, the system MUST:

1. Scan `output/runs/` directory for all existing run directories
2. Load each run's `metrics.json` file
3. Reconstruct the metrics counters from historical data
4. Populate `_run_history` array with all past runs
5. Set `runs_total`, `runs_completed`, etc. to correct values
6. Update `total_transactions_analyzed` and `total_fraud_detected` from cumulative data

## Required Fix

Add initialization method to `FraudSimMetrics`:

```python
class FraudSimMetrics:
    def __init__(self, output_dir: str = "./output/runs"):
        self._lock = threading.Lock()
        self._metrics = {
            'runs_total': 0,
            'runs_in_progress': 0,
            'runs_completed': 0,
            'runs_failed': 0,
            'last_run_accuracy': 0.0,
            'last_run_precision': 0.0,
            'last_run_recall': 0.0,
            'last_run_f1_score': 0.0,
            'total_transactions_analyzed': 0,
            'total_fraud_detected': 0,
            'pattern_flags': {}
        }
        self._run_history = []

        # CRITICAL: Load existing runs from disk
        self._load_existing_runs(output_dir)

    def _load_existing_runs(self, output_dir: str):
        """Load all existing runs from disk to restore metrics state"""
        import os
        import json
        from pathlib import Path

        if not os.path.exists(output_dir):
            return

        for run_dir in sorted(Path(output_dir).iterdir()):
            if not run_dir.is_dir() or not run_dir.name.startswith('run_'):
                continue

            metrics_file = run_dir / 'metrics.json'
            if not metrics_file.exists():
                continue

            try:
                with open(metrics_file, 'r') as f:
                    run_metrics = json.load(f)

                # Restore counters
                self._metrics['runs_total'] += 1
                if run_metrics['status'] == 'completed':
                    self._metrics['runs_completed'] += 1
                elif run_metrics['status'] == 'failed':
                    self._metrics['runs_failed'] += 1

                # Restore cumulative metrics
                self._metrics['total_transactions_analyzed'] += run_metrics['transaction_count']
                self._metrics['total_fraud_detected'] += run_metrics['detected_count']

                # Restore run history
                self._run_history.append({
                    'run_id': run_metrics['run_id'],
                    'fraud_type': run_metrics['fraud_type'],
                    'accuracy': run_metrics['accuracy'],
                    'precision': run_metrics['precision'],
                    'recall': run_metrics['recall'],
                    'f1_score': run_metrics['f1_score'],
                    'timestamp': run_metrics['timestamp']
                })

                # Update last run metrics (use most recent)
                self._metrics['last_run_accuracy'] = run_metrics['accuracy']
                self._metrics['last_run_precision'] = run_metrics['precision']
                self._metrics['last_run_recall'] = run_metrics['recall']
                self._metrics['last_run_f1_score'] = run_metrics['f1_score']

            except Exception as e:
                print(f"Warning: Failed to load run {run_dir.name}: {e}")
                continue
```

## Prevention Rules

### RULE 1: NEVER USE IN-MEMORY-ONLY METRICS FOR PERSISTENT SYSTEMS
All metrics that represent cumulative state MUST be persisted to disk or database.

### RULE 2: ALWAYS RELOAD STATE ON STARTUP
Any service that tracks state across requests MUST reload that state from persistent storage on initialization.

### RULE 3: VALIDATE METRICS AGAINST GROUND TRUTH
Before displaying metrics, verify they match the actual data on disk. If `available_runs` != `runs_total`, something is wrong.

### RULE 4: LOG METRIC INITIALIZATION
On startup, log:
```
Loaded 13 runs from disk
  - Card Testing: 10 runs
  - Velocity Attack: 1 run
  - Account Takeover: 1 run
  - Synthetic Identity: 1 run
Total transactions analyzed: 7800
Total fraud detected: 312
```

### RULE 5: FAIL FAST ON INCONSISTENCY
If disk state doesn't match memory state after initialization:
```python
if len(self._run_history) != self._metrics['runs_total']:
    raise RuntimeError(
        f"Metric inconsistency: {len(self._run_history)} runs in history "
        f"but runs_total={self._metrics['runs_total']}"
    )
```

## Testing Requirements

Before deploying ANY metric system:

1. **Test Case 1: Fresh Start**
   - Start server with empty `output/runs/`
   - Verify all metrics are 0
   - Execute 3 runs
   - Verify metrics show 3

2. **Test Case 2: Restart with Data**
   - Execute 5 runs
   - Stop server
   - Start server
   - **Verify metrics still show 5** ← THIS MUST PASS

3. **Test Case 3: Crash Recovery**
   - Execute 10 runs
   - Kill server (SIGKILL)
   - Start server
   - **Verify metrics show 10** ← THIS MUST PASS

4. **Test Case 4: Prometheus Scraping**
   - Execute runs
   - Restart server
   - Verify Prometheus sees correct cumulative values
   - Verify Grafana time-series graphs don't have gaps

## Files Affected

- `app/fraud_sim_api.py` - FraudSimMetrics class
- `run_fraud_sim_server.py` - Server initialization
- `app/run_manager.py` - Run persistence

## Accountability

This issue was introduced when implementing per-run history tracking. The `_run_history` array was added without considering server restart scenarios.

**Introduced in commit**: 6d61e035 "Add per-run comparison metrics and execute 10 test runs"

## Current Workaround

**NONE**. Data is lost. The only way to recover is to manually reconstruct metrics by reading all `metrics.json` files from disk.

## Next Steps

1. ⬜ Implement `_load_existing_runs()` method
2. ⬜ Add startup logging of loaded runs
3. ⬜ Add metric consistency validation
4. ⬜ Test restart scenarios
5. ⬜ Verify Grafana shows all 13 runs
6. ⬜ Document metric persistence in SETUP_DOCUMENTATION.md
7. ⬜ Add health check endpoint that validates disk vs memory consistency

## Related Issues

- Prometheus counters should NEVER decrease
- Grafana queries may show gaps in time-series data
- Run comparison charts missing historical data
- Pattern flag counts are incomplete

---

**LESSON LEARNED**: Any stateful service MUST persist and restore its state. In-memory-only state is NEVER acceptable for production systems that need to survive restarts.

**DO NOT DEPLOY THIS TO PRODUCTION UNTIL FIXED.**
