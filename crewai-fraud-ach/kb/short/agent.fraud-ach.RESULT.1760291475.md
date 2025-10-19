```json
{
  "id": "228ec09c58f7ed85",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291475,
  "host_pid": "9e6742732c60:1",
  "hash": "8019c05de9f4f7adff99222a71ec339e36ba1d4319d8dd765c40ce280c852298",
  "cid": "QmV18019c05de9f4f7adff99222a71ec339e36ba1d43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291475,
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
      "evaluated_at": 1760291475
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
  "sig": "7dce31987fb53064e497f076b1f79eef055e3448f8a55af94b507632f3ec798a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 77808192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}maly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8725948}}}