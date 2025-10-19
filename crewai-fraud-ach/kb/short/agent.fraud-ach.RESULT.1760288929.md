```json
{
  "id": "73b11611e190ce37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288929,
  "host_pid": "9e6742732c60:1",
  "hash": "d60f8f05fb81919691dd69a0ed12a9d51d5e059db6700bfc13046b1c2658939f",
  "cid": "QmV1d60f8f05fb81919691dd69a0ed12a9d51d5e059d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288929,
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
      "evaluated_at": 1760288929
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
  "sig": "55dde1edd45eaf31d02d25777f7647529c54400f9054c5ab12cfa6e3350604a3"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 122105153391998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 838583928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285764, 'matching_hash': '05c5de8ca533802c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.01, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7764666}}}