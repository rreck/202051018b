```json
{
  "id": "5cf3ed45cc3ba44d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289746,
  "host_pid": "9e6742732c60:1",
  "hash": "f59e4762e71bfbea8f369fe5990e98f13ef43cac4538b093d3e1bfa00eb05d25",
  "cid": "QmV1f59e4762e71bfbea8f369fe5990e98f13ef43cac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289746,
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
      "evaluated_at": 1760289746
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
  "sig": "29726efd95971f6f61a14dcc5028a8c0215fea1ee88af63da35c1876acc26001"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022696777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 64294824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'bb01014ea9b32f36'}}}