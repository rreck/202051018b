```json
{
  "id": "75ede6bd88eb07d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289603,
  "host_pid": "9e6742732c60:1",
  "hash": "0ffa9cbd82ecfad8d35cde3e93df5a0e58daf1e3c44c64fcf13a3d893c2b63b2",
  "cid": "QmV10ffa9cbd82ecfad8d35cde3e93df5a0e58daf1e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289603,
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
      "evaluated_at": 1760289603
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
  "sig": "952f436a3b3ba29110354b287e89a766221ce040dd3594e15a27a4bc89370a9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247162231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 35344768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '92769f469bceb512'}}}