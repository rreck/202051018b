```json
{
  "id": "4abd334841711b06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291664,
  "host_pid": "9e6742732c60:1",
  "hash": "155be28de7b0b4f2c90957b9486e2463b93a84821fd7719765eb03ff685a7b03",
  "cid": "QmV1155be28de7b0b4f2c90957b9486e2463b93a8482",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291664,
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
      "evaluated_at": 1760291664
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
  "sig": "7f0799d2b7e6e8eee4dfc614f5947d2275ab98bf1d8b91f5beefa0db599943eb"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000028604532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 1793982960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '4ce4a7b2afa8a7cc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.26, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9966572}}}