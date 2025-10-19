```json
{
  "id": "6aea0e750efbcada",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292269,
  "host_pid": "9e6742732c60:1",
  "hash": "1d467d098116a6394badc376a53245ed73f138d3ef44fd2f620bb3f1a8c5bfe3",
  "cid": "QmV11d467d098116a6394badc376a53245ed73f138d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292269,
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
      "evaluated_at": 1760292269
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
  "sig": "d9fa8dd4357e56659bb022c83c429bc67ec3ad08901ab2fd1aa3e4d9cb91083c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 91145274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}