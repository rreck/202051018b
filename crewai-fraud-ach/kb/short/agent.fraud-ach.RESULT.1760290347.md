```json
{
  "id": "89e3576c0677d12e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290347,
  "host_pid": "9e6742732c60:1",
  "hash": "8228abe78deee01a7f1120196a5be8e8179766f64154c186497947e97f7dbffd",
  "cid": "QmV18228abe78deee01a7f1120196a5be8e8179766f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290347,
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
      "evaluated_at": 1760290347
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
  "sig": "c9489019947eba35531a21bad2f29f93c2fc6efa6ed26f104f33980ca22f37a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 16095444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}