```json
{
  "id": "afa19fd23e56de0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288058,
  "host_pid": "9e6742732c60:1",
  "hash": "2c1b67b7fb99b16680a3b49c374141164e58f5047a5d2cf5a594cb7f1000f8d2",
  "cid": "QmV12c1b67b7fb99b16680a3b49c374141164e58f504",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288058,
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
      "evaluated_at": 1760288058
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
  "sig": "1914bc3e798e142af0f279bb1eca67d841418cd0772626e04a2e3f52cd552510"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 11404314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}