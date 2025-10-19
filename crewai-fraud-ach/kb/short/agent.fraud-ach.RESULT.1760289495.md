```json
{
  "id": "4e078e4726f5ec87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289495,
  "host_pid": "9e6742732c60:1",
  "hash": "4921babae6b2f18864bcbd60ffb8fc278bfe0ee9612dc8149be3d8cc8ab2e992",
  "cid": "QmV14921babae6b2f18864bcbd60ffb8fc278bfe0ee9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289495,
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
      "evaluated_at": 1760289495
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
  "sig": "a6ff33f39c0ab65c8919dc631ac5de9ba761b028aeb72668d2af07d6e060ce0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033919598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 47113625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '1dbf667d29bdf8b7'}}}