```json
{
  "id": "2088807828ac79e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294048,
  "host_pid": "9e6742732c60:1",
  "hash": "b7f9b280c0e903b4633df7fc48b902fa8b6b8d3de58ef824abab1ee67d9a7836",
  "cid": "QmV1b7f9b280c0e903b4633df7fc48b902fa8b6b8d3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294048,
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
      "evaluated_at": 1760294048
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
  "sig": "d841ce134e2f628a4b82a089b288756c37f432987f8be9da1edae00df4ca1d76"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 73197040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}