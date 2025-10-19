```json
{
  "id": "8e68b066841949aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292598,
  "host_pid": "9e6742732c60:1",
  "hash": "e71b1c86611f7a22f42b2a2979564e980a332376d7cef7404323f1b5531417b3",
  "cid": "QmV1e71b1c86611f7a22f42b2a2979564e980a332376",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292598,
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
      "evaluated_at": 1760292598
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
  "sig": "dbdc225e9ea2602844f29b43bf397bcfa8c61a4423a1b5ca828b607b810be18b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 88377690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}