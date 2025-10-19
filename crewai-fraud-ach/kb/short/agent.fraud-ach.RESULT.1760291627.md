```json
{
  "id": "07b14051d224875a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291627,
  "host_pid": "9e6742732c60:1",
  "hash": "978213b39f1a6b9c3d8854a9349c54f1f3921e9155bc10cae11e3f6957b2b54c",
  "cid": "QmV1978213b39f1a6b9c3d8854a9349c54f1f3921e91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291627,
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
      "evaluated_at": 1760291627
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
  "sig": "bc92873eb01b4c88797a15e4d1c7984b748ff7be82cfb687fb373147de2facbe"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105153391998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 1389875214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285764, 'matching_hash': '05c5de8ca533802c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.01, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7764666}}}