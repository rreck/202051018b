```json
{
  "id": "da53753c1b24ad71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293615,
  "host_pid": "9e6742732c60:1",
  "hash": "e808d2ad4963671c5b2c730ffc57ff10e1d5e363ab6c6a369e9b689ba08bf56f",
  "cid": "QmV1e808d2ad4963671c5b2c730ffc57ff10e1d5e363",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293615,
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
      "evaluated_at": 1760293615
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
  "sig": "d3a0260d17cefecdf72f13dfa8c8a4aff3b4c63d63a7cb094b11e05d0fa36c70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247109361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 21012966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '3efad933d2b7f9bd'}}}