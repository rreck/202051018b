```json
{
  "id": "fc6323af77e9a261",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289517,
  "host_pid": "9e6742732c60:1",
  "hash": "2a8d8a161726b1716e139207b0cf673fa8edc4f8a735bb4a20c13594fbbf63c7",
  "cid": "QmV12a8d8a161726b1716e139207b0cf673fa8edc4f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289517,
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
      "evaluated_at": 1760289517
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
  "sig": "be49ef0ce35f2f17ac6b9aeb151a4e9fd99448b2e31d9737f3a2f84ec1bb6980"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033294426
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 18076250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': '591497f4da3dc787'}}}