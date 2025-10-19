```json
{
  "id": "claude.TASK.1760886964",
  "scope": "claude",
  "key": "TASK",
  "epoch": 1760886964,
  "host_pid": "rreck-MS-7D25_9529",
  "hash": "2458c13627264f262d98e03bd61087bfceeae2ba30448eb0b46572ed95db",
  "cid": "bafkreiht5z7qxw2vkjn4y3r5m6pq8s9t2u3v4w5x6y7z8a9b0c1d2e3f4g5",
  "aicp": {
    "prov": {
      "issuer": "did:claude:sonnet-4-5-20250929",
      "issued": "2025-10-19T00:00:00Z",
      "proof": "ed25519:stub"
    },
    "ucon": {
      "constraints": ["no-external-systems", "local-only", "test-data-only"],
      "obligations": ["track-artifacts", "document-decisions"]
    },
    "eval": {
      "risk": "low",
      "classification": "development",
      "review_required": false
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {
    "priority": "high",
    "complexity": "medium"
  },
  "thresholds": {},
  "tags": ["crewai-fraud-ach", "synthetic-data", "card-testing", "simulation", "grafana"],
  "sig": "stub_signature"
}
```

# Task: Build Card Testing Fraud Simulation Capability

## Objective
Implement run-based fraud simulation system for crewai-fraud-ach agent enabling user-initiated card testing fraud scenarios with synthetic data generation and detection visualization.

## Requirements
1. Copy crewai-fraud-ach agent from `/home/rreck/Desktop/20251012a/` to current workspace
2. Generate synthetic transaction data matching 151-column schema with realistic distributions
3. Inject card testing fraud patterns into synthetic data batches
4. Implement scoring system (0-100) with configurable threshold (default 75)
5. Add pattern flag detection with specific triggers:
   - `card_testing_rapid_succession`: 5+ txns under $5 in <10 minutes
   - `card_testing_amount_pattern`: Ascending small amounts
   - `card_testing_mixed_decline_approve`: Multiple declines → approvals
   - `card_testing_merchant_diversity`: Same card, 3+ merchants quickly
   - `card_testing_velocity`: >10 txns/hour same card
6. Create run management via A2A API endpoints
7. Output CSV files to `output/runs/<runid>/`
8. Add new Grafana dashboard (preserve existing 6-panel dashboard)
9. Expose Prometheus metrics for runs, scores, patterns, confusion matrix
10. Test complete workflow

## Constraints
- DO NOT modify existing fraud-ach-dashboard.json
- DO NOT use real fraud data
- All data synthetic only
- Follow CLAUDE.md architecture patterns
- Maintain A2A API compliance

## Success Criteria
- User can initiate run with fraud type parameter
- System generates clean + fraudulent CSV
- Detection achieves >90% accuracy on injected fraud
- Dashboard shows scoring distribution + pattern flags + confusion matrix
- pmem artifacts track run learnings
