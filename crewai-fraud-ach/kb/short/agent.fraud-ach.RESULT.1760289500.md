```json
{
  "id": "c387d7b2c37508fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289500,
  "host_pid": "9e6742732c60:1",
  "hash": "92d9e2b0bdb6da24ee8a8c1d160c8c819468cfdd7f36044d632e1abefac0e50b",
  "cid": "QmV192d9e2b0bdb6da24ee8a8c1d160c8c819468cfdd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289500,
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
      "evaluated_at": 1760289500
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
  "sig": "b568871cecb8ed58d178456657691b1c060aefab3bb731d67b5492f757384a9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 10242000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8052182}}}