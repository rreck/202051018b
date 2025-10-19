```json
{
  "id": "1d543931ffbbee27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289436,
  "host_pid": "9e6742732c60:1",
  "hash": "9b5aebc6d12e29fc31ed9d6b9dad0651e7eb1f6eb81b71f31ff3d640e076e2b1",
  "cid": "QmV19b5aebc6d12e29fc31ed9d6b9dad0651e7eb1f6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289436,
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
      "evaluated_at": 1760289436
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
  "sig": "2f51c96392276889e20fd0f1fac6f183c7a91e6a33ccbae63c984b20f8f5dd00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 52547542, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}