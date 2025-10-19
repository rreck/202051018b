```json
{
  "id": "a3df16d69ba3fd55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289749,
  "host_pid": "9e6742732c60:1",
  "hash": "1d608ac5be88d0f280394998966c5012906eabc1daa8730d21b0dc475b6fb9d4",
  "cid": "QmV11d608ac5be88d0f280394998966c5012906eabc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289749,
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
      "evaluated_at": 1760289749
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
  "sig": "bcf86b90a25860e89a5e8cdaec172bc39d69f0ac85ad14121abf8618b19d09cd"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 907549632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}