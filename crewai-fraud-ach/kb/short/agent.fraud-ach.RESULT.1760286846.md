```json
{
  "id": "d1a7a8552e167d87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286846,
  "host_pid": "9e6742732c60:1",
  "hash": "40c63cdc9cab310e9b7bb39762cc49b53f9c98d3390ff6989b382b6425061c84",
  "cid": "QmV140c63cdc9cab310e9b7bb39762cc49b53f9c98d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286846,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286846
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "92a27e7349116447cad01621d3ed626269a3cb2debffe5ad1f1995d4d0483317"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279407211
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}