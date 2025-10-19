```json
{
  "id": "a002711f63051b1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290228,
  "host_pid": "9e6742732c60:1",
  "hash": "52d4f4cca3f4cf780793381e54d4b275f0bd4fc95215c5d7c328badba77b27a3",
  "cid": "QmV152d4f4cca3f4cf780793381e54d4b275f0bd4fc9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290228,
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
      "evaluated_at": 1760290228
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
  "sig": "a6cac3c91017aba8deabd670b4c29bcf9b3c70fbb4a66d8923d9450778a8ba75"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 031201463227855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 1325974395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'a9c92113e6dbf136'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9144651}}}