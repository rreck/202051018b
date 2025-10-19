```json
{
  "id": "9db266f08cffd210",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291398,
  "host_pid": "9e6742732c60:1",
  "hash": "3d8d1f509b995a5937b7c370165a2d9d339c8662aab51a098e3315d6e3bf8f20",
  "cid": "QmV13d8d1f509b995a5937b7c370165a2d9d339c8662",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291398,
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
      "evaluated_at": 1760291398
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
  "sig": "4d31d1f915e548748c04c5a5f210f0006793bf70c5063240943255fdb83a840e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469153369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 15794328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': 'a6e88c6efc20349f'}}}