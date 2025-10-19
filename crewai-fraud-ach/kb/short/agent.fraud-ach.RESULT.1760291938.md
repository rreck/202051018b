```json
{
  "id": "7db4d2d1244a5563",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291938,
  "host_pid": "9e6742732c60:1",
  "hash": "39a529a4122e4306bea6db2fc65a68ff436a6555e71804fe525d2d59539a34cf",
  "cid": "QmV139a529a4122e4306bea6db2fc65a68ff436a6555",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291938,
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
      "evaluated_at": 1760291938
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
  "sig": "dea08796b7e47bfdff45c3af353c72e03c1b0ae4d9fe614c9d07f51794747ba9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 18827292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}