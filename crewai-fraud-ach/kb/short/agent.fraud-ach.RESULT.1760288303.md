```json
{
  "id": "4cebc1e7a1748af7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288303,
  "host_pid": "9e6742732c60:1",
  "hash": "ef4fa48b06b2a6ea27ad9c301955e1ccce7f98aa8ffebc130b9ef8e578c3c70d",
  "cid": "QmV1ef4fa48b06b2a6ea27ad9c301955e1ccce7f98aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288303,
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
      "evaluated_at": 1760288303
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
  "sig": "fc0d392fe69a4e4724240d371d4065b66259fb60c59f6c790f8d93708501716a"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000021698868
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 934400775, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760284979, 'matching_hash': '4224f1af7034834c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5663035}}}