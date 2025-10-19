```json
{
  "id": "66d35339a8ac98ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286070,
  "host_pid": "9e6742732c60:1",
  "hash": "f2733d70ce44b0bd28ad614bd20e437747ba0ff15c84189b13d9ac4c4d65a8f6",
  "cid": "QmV1f2733d70ce44b0bd28ad614bd20e437747ba0ff1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286070,
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
      "evaluated_at": 1760286070
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "30faab08e471e5007a7f544003f1428223beba23136f85305dfb4cb1ef9535d1"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 82325971, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6332767}}}