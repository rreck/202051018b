```json
{
  "id": "a9bc3a0034bdc2ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289481,
  "host_pid": "9e6742732c60:1",
  "hash": "183e0bf56b8a6072a5f980c14ecfe79ba139071cf18ca27b2c4bbe375e93b3ab",
  "cid": "QmV1183e0bf56b8a6072a5f980c14ecfe79ba139071c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289481,
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
      "evaluated_at": 1760289481
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
  "sig": "253758a0288a6369a89a90e60d64a34f29528777b4b015be2a09f2917cac877b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 45637456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}