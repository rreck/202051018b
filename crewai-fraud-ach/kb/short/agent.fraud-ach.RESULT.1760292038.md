```json
{
  "id": "87f0becd5a62fb48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292038,
  "host_pid": "9e6742732c60:1",
  "hash": "ce6b29072d695cffe702f5310a47fd48055625a76903a76795e0fb16d93c009a",
  "cid": "QmV1ce6b29072d695cffe702f5310a47fd48055625a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292038,
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
      "evaluated_at": 1760292038
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
  "sig": "45ddbb6d297f3cff530b4bd5e1b3d7a9d7316593357faf7e37ef9900256c5692"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009592950397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 1758959496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '5b23ebe5172c1d5f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9306664}}}