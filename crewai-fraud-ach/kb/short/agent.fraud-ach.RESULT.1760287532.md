```json
{
  "id": "0e022e309e617a5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287532,
  "host_pid": "9e6742732c60:1",
  "hash": "4c90f4ef428c6605037e2cdc55ac17537c51d4af70f5ac8f5b934bd36b0d37f5",
  "cid": "QmV14c90f4ef428c6605037e2cdc55ac17537c51d4af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287532,
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
      "evaluated_at": 1760287532
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
  "sig": "9004fcab88c4cd2335bdd8d9459429ef95beb722bd25998fa49432323af91d32"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 12408984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}