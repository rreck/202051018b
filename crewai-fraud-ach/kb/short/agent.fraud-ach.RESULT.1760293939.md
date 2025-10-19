```json
{
  "id": "6578179a57a5d774",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293939,
  "host_pid": "9e6742732c60:1",
  "hash": "7297f2fe017309a9cc944bd087baa4b4ea7b9aa73eeeedd6ea09ac887b53defa",
  "cid": "QmV17297f2fe017309a9cc944bd087baa4b4ea7b9aa7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293939,
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
      "evaluated_at": 1760293939
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
  "sig": "4abc0f3c1dd83166af63283792ecfd8274451d36532916f3c4014b3d05924907"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000026237439
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1245364956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': '88704d1e07f02084'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5462127}}}