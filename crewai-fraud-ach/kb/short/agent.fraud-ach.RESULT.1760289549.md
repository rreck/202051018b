```json
{
  "id": "7d4a277f1c9f0a31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289549,
  "host_pid": "9e6742732c60:1",
  "hash": "19564f7d89ff0bba610ca37195793b69d3a509c61acc30d4de3ca3997262e0ef",
  "cid": "QmV119564f7d89ff0bba610ca37195793b69d3a509c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289549,
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
      "evaluated_at": 1760289549
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
  "sig": "948ac802d75c900d111e69ade10239b25a0155e0226184b9a753cab762400a3b"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 1186560774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9417149}}}