```json
{
  "id": "e3c4f897ecf2a25f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291488,
  "host_pid": "9e6742732c60:1",
  "hash": "36ea4753db80830ff5800271234dfabf92e45acdbeb79ee1c7997bc98788e9ea",
  "cid": "QmV136ea4753db80830ff5800271234dfabf92e45acd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291488,
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
      "evaluated_at": 1760291488
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
  "sig": "80da1285d55aac1af353a3649321a6f49dd8554e236b6976464c83d398422675"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 026009594219462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 898526816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '4d9d7d0d036b9510'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5105266}}}