```json
{
  "id": "03ed5a5be9d489f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288299,
  "host_pid": "9e6742732c60:1",
  "hash": "09f5ee27469176d046ce18a2e49cd7d1a55ca216ce2f536effdf90593949da32",
  "cid": "QmV109f5ee27469176d046ce18a2e49cd7d1a55ca216",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288299,
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
      "evaluated_at": 1760288299
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "98884ff85187f2d2a54851c78de0d7072bd3a5f9d8712fc936361a3e16bc16a6"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000025025802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 713630925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285764, 'matching_hash': 'd7be7bb127c676c6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8018325}}}