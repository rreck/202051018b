```json
{
  "id": "00f6749ce19a5668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289185,
  "host_pid": "9e6742732c60:1",
  "hash": "c44463d8f58a1fd493bf688930a1ea4ecf3f84108fb48a0659f8f5ed446e9045",
  "cid": "QmV1c44463d8f58a1fd493bf688930a1ea4ecf3f8410",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289185,
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
      "evaluated_at": 1760289185
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
  "sig": "9a4769a870b28bbcbccdb3e875d04535009f329807f63acbe8a17ce9ba3ba31e"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105154811722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 869266880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': 'f2f6645498600029'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7493680}}}