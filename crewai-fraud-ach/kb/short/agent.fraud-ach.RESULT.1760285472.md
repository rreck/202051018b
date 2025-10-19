```json
{
  "id": "1a31f17e37f9ec8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285472,
  "host_pid": "9e6742732c60:1",
  "hash": "2f40096f27ee6c5842d231c89c40ca240fd3565b729ea717351f2f0534d13c67",
  "cid": "QmV12f40096f27ee6c5842d231c89c40ca240fd3565b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285472,
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
      "evaluated_at": 1760285472
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c6ea6b0694a83b699a54bdb9693d395c7d43d0601c986b303b1725f2f1b78f90"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20648306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}