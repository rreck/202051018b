```json
{
  "id": "f81b1106838717c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292498,
  "host_pid": "9e6742732c60:1",
  "hash": "ad1cea1c73fa8c382379e2162d8616f27afdd060686e8eee720e006536b70620",
  "cid": "QmV1ad1cea1c73fa8c382379e2162d8616f27afdd060",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292498,
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
      "evaluated_at": 1760292498
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
  "sig": "6b42152f01faca3c3f8512f7a0068e0ef3d596237f1db4cc8d0b2f616bbcc019"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 15220714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}