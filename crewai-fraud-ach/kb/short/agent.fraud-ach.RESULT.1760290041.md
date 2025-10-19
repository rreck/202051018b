```json
{
  "id": "c74e37b2ef8dc85b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290041,
  "host_pid": "9e6742732c60:1",
  "hash": "d7f9871fe4c164ab797d7532c2eff51b16089cfd33a8a5e36b59c0d600175e65",
  "cid": "QmV1d7f9871fe4c164ab797d7532c2eff51b16089cfd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290041,
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
      "evaluated_at": 1760290041
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
  "sig": "9a6427da2d8a50b2d7b4502ee314f006c4bbc198167302d971935331a468bda6"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105150872647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 1009311240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'f142eb53d77ea00a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7209366}}}