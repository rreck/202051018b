```json
{
  "id": "f420e206372331c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288832,
  "host_pid": "9e6742732c60:1",
  "hash": "aed6ff905778213f7c48c7a3a83b9766c58e1c5c9c03311d9ee3b54e9127758a",
  "cid": "QmV1aed6ff905778213f7c48c7a3a83b9766c58e1c5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288832,
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
      "evaluated_at": 1760288832
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
  "sig": "3db9d0aa7229113fbd206675ae1cba81ce249d8e3b060e5a26e51db72605d802"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000024248654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 814164645, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': '6adb7b11c0829b91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7753949}}}