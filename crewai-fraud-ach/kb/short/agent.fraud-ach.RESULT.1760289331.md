```json
{
  "id": "1f560914a176ea37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289331,
  "host_pid": "9e6742732c60:1",
  "hash": "d4f168766ec7d298c11c0402b088ebab92b6898d4b5881a5f880a925b33579f9",
  "cid": "QmV1d4f168766ec7d298c11c0402b088ebab92b6898d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289331,
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
      "evaluated_at": 1760289331
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
  "sig": "0786b113f339df19791c8e61fd93216067354394eb9faf95756daa45d5dd6232"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000028604532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 1195988640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': '4ce4a7b2afa8a7cc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.26, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9966572}}}