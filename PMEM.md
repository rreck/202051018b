# pmem 1.0 - Persistent Memory System

Biomimicry-driven, auditable, on-prem persistent memory system enabling emergent group-think via structured files, reinforced links, and governed synthesis across agents.

## Architecture

### Directory Structure
```
.
├── kb/
│   ├── short/      # Atomic artifacts: IDEA, TASK, PROBLEM, ACTION, RESULT, LESSON
│   └── long/       # Emergent artifacts: CLUSTER, SYNTHESIS, META, ECHO, CONSENSUS
├── pmem.py         # Core library
├── pmem_consolidate.py  # Consolidation engine
└── pmem_demo.py    # Demo workflow
```

### File Naming Convention
**Strict format:** `<scope>.<KEY>.<EPOCH>.md`

- **scope**: `agent` | `crew`
- **KEY**: IDEA, TASK, PROBLEM, ACTION, RESULT, LESSON, CLUSTER, SYNTHESIS, META, ECHO, CONSENSUS
- **EPOCH**: Unix timestamp in seconds

Examples:
- `agent.IDEA.1760798654.md`
- `crew.CONSENSUS.1760798654.md`

### File Structure
Every artifact contains:
1. **JSON header block** (machine-readable metadata)
2. **Markdown body** (human-readable content)

```markdown
```json
{
  "id": "agent.IDEA.1760798654",
  "scope": "agent",
  "key": "IDEA",
  "epoch": 1760798654,
  "host_pid": "hostname:12345",
  "hash": "sha256...",
  "cid": "cid:...",
  "aicp": { ... },
  "sources": [...],
  "edges": [...],
  "metrics": { ... },
  "thresholds": { ... },
  "tags": [...],
  "sig": "sha256..."
}
```

# Artifact Body
Content goes here...
\```

## Key Components

### Atomic Artifacts (kb/short)
Direct observations and actions, ≤64 KB:
- **IDEA**: Concepts, proposals, hypotheses
- **TASK**: Work items, assignments
- **PROBLEM**: Issues, challenges, blockers
- **ACTION**: Steps taken, commands executed
- **RESULT**: Outcomes, outputs, findings
- **LESSON**: Learnings, insights, patterns

### Emergent Artifacts (kb/long)
Synthesized knowledge, ≤512 KB:
- **CLUSTER**: Groups of related artifacts meeting weight thresholds
- **SYNTHESIS**: Cross-cluster patterns and hypotheses
- **META**: Meta-rules derived from syntheses
- **ECHO**: Anomaly detection and quarantine candidates
- **CONSENSUS**: Quorum-based agreements for propagation

## AICP Headers

Every artifact includes AI Content Provenance:

### AICP-PROV (Provenance)
Verifiable Credential with issuer, timestamp, and cryptographic signature

### AICP-UCON (Usage Control)
Constraints, obligations, and permissions governing artifact usage

### AICP-EVAL (Evaluation)
Quality metrics, confidence scores, reviewer information

## Edge System

### Bidirectional Links
- Source and target artifact IDs
- Weight w ∈ [0, 1]
- Last update timestamp

### Weight Decay
Exponential decay: w(t) = w₀ × e^(-λt)
- λ = 0.01/day
- Edges pruned when w < 0.001

### Co-occurrence Window
- τ = 7 days
- Reinforcement events must occur within window

## Consolidation Rules

### CLUSTER Formation
**Required:**
- ≥5 unique sources
- Average weight ≥0.6
- All sources within co-occurrence window

**Output:**
- Summary of pattern
- Member list with weights
- Governance metadata
- Next steps

### SYNTHESIS Generation
**Required:**
- ≥2 clusters
- Jensen-Shannon divergence ≤0.25
- No UCON conflicts

**Output:**
- Theme and hypothesis
- Evidence from clusters
- Heuristics and limitations

### META Derivation
**Required:**
- ≥2 syntheses
- Cross-synthesis coherence

**Output:**
- Meta-rule statement
- Supporting syntheses
- Standard definition
- Impact assessment

### ECHO Analysis
**Purpose:** Anomaly detection, NOT used as source

**Output:**
- Replay description
- Mutation patterns
- Anomaly list (z-score > 2.0)
- Quarantine candidates

### CONSENSUS Building
**Required:**
- Quorum ≥67%
- No UCON conflicts
- All sources verified

**Output:**
- Position statement
- Rationale
- Quorum metrics
- Action approval

## Usage Examples

### Create Atomic Artifact
```python
from pmem import PMemSystem

pmem = PMemSystem()

filepath = pmem.write_artifact(
    scope="agent",
    key="IDEA",
    body="Implement distributed edge graph",
    tags=["architecture", "distributed"],
    metrics={"priority": 0.9},
    issuer="my-agent"
)
```

### Add Edge
```python
pmem.add_edge(
    source_id="agent.IDEA.1760798654",
    target_id="agent.TASK.1760798655",
    weight=0.85
)
```

### Run Consolidation
```python
from pmem_consolidate import PMemConsolidator

consolidator = PMemConsolidator(pmem)
stats = consolidator.run_consolidation()
# Returns: {"clusters": N, "syntheses": M, ...}
```

### Verify Provenance
```python
is_valid = pmem.verify_provenance(filepath)
# Returns: True if AICP-PROV verified and hash matches
```

## Constraints & Rules

### MUST
1. Use strict filename format
2. Include complete JSON header in every file
3. Maintain cryptographic provenance
4. Track bidirectional links with weights
5. Apply co-occurrence window for reinforcement
6. Run consolidation when thresholds met
7. Emit AICP headers (PROV, UCON, EVAL)
8. Store atomics in kb/short, emergent in kb/long
9. Log all actions with EPOCH, actor, host, PID

### MUST NOT
1. Modify source files post-issuance (create new EPOCH instead)
2. Create emergent artifacts without listing sources
3. Strip UCON, proofs, or issuer metadata
4. Merge clusters across agents without explicit rule
5. Store secrets or PII in bodies
6. Use non-JSON headers or mixed formats
7. Use ECHO artifacts as sources

### Thresholds
- Co-occurrence window: τ = 7 days
- Weight decay: λ = 0.01/day
- Weight range: w ∈ [0, 1]
- Cluster min sources: 5
- Cluster min weight: 0.6
- Synthesis min clusters: 2
- Synthesis max JS divergence: 0.25
- Consensus min quorum: 67%
- Update threshold: Δw ≥ 0.05
- Atomic file size: ≤64 KB
- Emergent file size: ≤512 KB

## Termination Conditions

Consolidation stops when:
- No edges update by Δw ≥ 0.05
- No new clusters form
- All anomalies triaged
- All artifacts signed and verified

## Security & Governance

### Provenance Chain
Every artifact traces back to:
- Issuing agent
- Creation timestamp
- Host and process ID
- Source artifacts (if emergent)

### Signature Verification
Hash computed over:
- Artifact body (stripped and normalized)
- Header metadata (with sig="")

### UCON Enforcement
- Constraints checked before consensus
- Conflicts block emergent artifact creation
- Permissions enforced at read/write

### Immutability
- Files never modified after creation
- Updates create new EPOCH version
- Consensus frozen upon signing
- Lineage permanently recorded

## Integration with Agents

### Agent Workflow
1. Agent creates atomic artifacts (IDEA, TASK, ACTION, RESULT)
2. Edges form through temporal co-occurrence
3. Consolidation jobs run periodically
4. Clusters emerge from weighted edges
5. Synthesis spans multiple clusters
6. Consensus achieved across agents
7. Knowledge propagates via approved artifacts

### Multi-Agent Setup
- Each agent writes to own scope: `agent.*`
- Crew-level consolidation creates: `crew.*`
- Cross-agent consensus requires quorum
- UCON prevents unauthorized propagation

## Testing

Run the demo:
```bash
python3 pmem_demo.py
```

Expected output:
- 5 IDEAs created
- 5 TASKs from ideas
- 5 RESULTs from tasks
- Edges tracked and weighted
- CONSENSUS achieved
- All provenance verified (16/16)

## Files

- **pmem.py**: Core system (420 lines)
- **pmem_consolidate.py**: Consolidation engine (270 lines)
- **pmem_demo.py**: Complete workflow demo (200 lines)

## Version

pmem 1.0 - 2025-10-18

## References

- W3C Verifiable Credentials: https://www.w3.org/2018/credentials/v1
- Content-addressable storage
- Jensen-Shannon divergence for cluster coherence
- Temporal co-occurrence reinforcement learning
