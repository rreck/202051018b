```json
{
  "id": "9f374daa16b23606",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289482,
  "host_pid": "9e6742732c60:1",
  "hash": "0d4d0d7702b91219683e06285e0d657ff8d43614314ef3fbe4eac92685a86cf2",
  "cid": "QmV10d4d0d7702b91219683e06285e0d657ff8d43614",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289482,
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
      "evaluated_at": 1760289482
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
  "sig": "70eba1b242085207ff96ca761a3a6ddc9266ed9aca10910067b238ccb9d75a7d"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000028976117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 738001252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': 'f0572624c8eaf0e8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5951623}}}