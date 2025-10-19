```json
{
  "id": "8203e4f0602f183e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292900,
  "host_pid": "9e6742732c60:1",
  "hash": "d66d7d4b4ecb6d6d5fca4a5d5dfcb85af9df55454046cb09f7d2171cf89c31fc",
  "cid": "QmV1d66d7d4b4ecb6d6d5fca4a5d5dfcb85af9df5545",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292900,
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
      "evaluated_at": 1760292900
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
  "sig": "d6733d0a87d3e7cf1af219fc0f9197ce8361997325814ba0acebf569e3271c3c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 1160178282, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5604726}}}