```json
{
  "id": "4b9aa1b8048a8daa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293439,
  "host_pid": "9e6742732c60:1",
  "hash": "bd0a5c1ed87ed6ae025268c84e3f02b4b362252ffde5597a459b7d267879d6cd",
  "cid": "QmV1bd0a5c1ed87ed6ae025268c84e3f02b4b362252f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293439,
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
      "evaluated_at": 1760293439
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
  "sig": "b7d9121f4cfd60fd655b5f73cb914b74bdc11d49a7d8b9f6fe3cc783eb37f4ec"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000025312922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 1253451168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': 'ec5c02804d9cd63b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5749776}}}