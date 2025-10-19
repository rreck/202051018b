```json
{
  "id": "f9fcb92ef764be88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289411,
  "host_pid": "9e6742732c60:1",
  "hash": "edaaa562c5f88b98f6ad5ce8d33d644b8e696974dd4d094a86a7b93b94bb6322",
  "cid": "QmV1edaaa562c5f88b98f6ad5ce8d33d644b8e696974",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289411,
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
      "evaluated_at": 1760289411
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
  "sig": "26abe7b285cad393da0192d89e699871a1aa3a1a05ac26954a9a3493c26ed942"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 20966066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}