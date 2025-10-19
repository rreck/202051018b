```json
{
  "id": "3c314c11fddbe766",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292477,
  "host_pid": "9e6742732c60:1",
  "hash": "bc53fd1b5dae11a4505038e3c95b7c27eafe0fde6959bfa14605b289f07c7043",
  "cid": "QmV1bc53fd1b5dae11a4505038e3c95b7c27eafe0fde",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292477,
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
      "evaluated_at": 1760292477
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
  "sig": "8d8ab2936d3e999d7a7d56b8c4c45a328e631d6dabc08e781f550711f6e95a48"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247499118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 15146604, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}