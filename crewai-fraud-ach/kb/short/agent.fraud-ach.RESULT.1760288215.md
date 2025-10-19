```json
{
  "id": "a6b05eadf8199fab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288215,
  "host_pid": "9e6742732c60:1",
  "hash": "35c5aecbc79cf5feab45aa1ed3bcf95af60853a255a52be8cbe5f45e97f4e03c",
  "cid": "QmV135c5aecbc79cf5feab45aa1ed3bcf95af60853a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288215,
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
      "evaluated_at": 1760288215
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
  "sig": "5700a810ce229e9f085822e005063f9c1e7f9028520b71af98e8ec0d76469dbb"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100272253110
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 592668054, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285764, 'matching_hash': 'c9de6cf87e9b501f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6891489}}}