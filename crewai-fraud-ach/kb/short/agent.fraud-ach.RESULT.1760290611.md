```json
{
  "id": "483afccc4ead2d17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290611,
  "host_pid": "9e6742732c60:1",
  "hash": "48386b83e8cd2ea4fa2a9f2830b46f9e6e7a9884a7f7fe4fdba2cb797f9ced4b",
  "cid": "QmV148386b83e8cd2ea4fa2a9f2830b46f9e6e7a9884",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290611,
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
      "evaluated_at": 1760290611
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
  "sig": "8a508eb71f79ae360db7cf2432b61fdeaed525a3fe7aacdf8e8d6d288264f9f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595856880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 48467415, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '3e252270c9e333bc'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.27, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6465420}}}