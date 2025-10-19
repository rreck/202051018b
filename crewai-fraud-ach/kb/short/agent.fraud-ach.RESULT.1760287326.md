```json
{
  "id": "fbf95b81f533ac15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287326,
  "host_pid": "9e6742732c60:1",
  "hash": "36b4580d065006ca8de2097ca057ec952f1dbcc4751cf978402096ede806f521",
  "cid": "QmV136b4580d065006ca8de2097ca057ec952f1dbcc4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287326,
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
      "evaluated_at": 1760287326
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
  "sig": "60e24cd32d8d9df683b9c67e68ee444ef4216b46f20a996298f4975141c3ddb6"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241978752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 12521768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}