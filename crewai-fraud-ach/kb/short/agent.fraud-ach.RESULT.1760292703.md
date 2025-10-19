```json
{
  "id": "0006b35ae83a3012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292703,
  "host_pid": "9e6742732c60:1",
  "hash": "9cf634223af03731d9d8707ca75c1087a619fc303d0c7fa509943fdb5edbb3f3",
  "cid": "QmV19cf634223af03731d9d8707ca75c1087a619fc30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292703,
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
      "evaluated_at": 1760292703
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
  "sig": "361c92a016ede01fa76a92bbe2bbbd954263b89a99373e0e7208a68bcad6e692"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 99574748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}