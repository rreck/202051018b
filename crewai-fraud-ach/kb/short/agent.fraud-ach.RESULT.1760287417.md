```json
{
  "id": "3a62bbf7b74f5df0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287417,
  "host_pid": "9e6742732c60:1",
  "hash": "80d974341bd90c51a4ccd29b12a5ed9e002a558c4f03d5aa6a4c88bfc5d0e838",
  "cid": "QmV180d974341bd90c51a4ccd29b12a5ed9e002a558c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287417,
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
      "evaluated_at": 1760287417
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "cd1f3319716cf183559bde3faeb61db5caecc0b9e4b938d6a91fdd733f95f278"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 25820406, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}