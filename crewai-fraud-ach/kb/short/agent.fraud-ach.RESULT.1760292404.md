```json
{
  "id": "71b1951852908199",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292404,
  "host_pid": "9e6742732c60:1",
  "hash": "bc7a9494307bb458f8ecd79fd01ea1e16248d467c774af6b1a723ea5a20039d1",
  "cid": "QmV1bc7a9494307bb458f8ecd79fd01ea1e16248d467",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292404,
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
      "evaluated_at": 1760292404
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
  "sig": "40c16aa7210e12d4ed70e56ffca830188245a976fbe76c632eb07e1bb949c92d"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000023922367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 1173412573, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '420dc08dc8ad4808'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5956409}}}