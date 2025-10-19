```json
{
  "id": "3f4a85b122c4d47f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294115,
  "host_pid": "9e6742732c60:1",
  "hash": "cd8be18ac3ff4b13fb83a2eb1458fc1028a9b01978faadc3e93a848c9195c9c9",
  "cid": "QmV1cd8be18ac3ff4b13fb83a2eb1458fc1028a9b019",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294115,
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
      "evaluated_at": 1760294115
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "60bf19dda38732cc241eeb8f07c150ec70571ccc6b88f61031b7498080b5e611"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462075291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 73297848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '75f7f0ceec197518'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}