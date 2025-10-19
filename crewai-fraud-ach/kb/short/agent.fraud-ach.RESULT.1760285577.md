```json
{
  "id": "2a7f5cf4ef2b88dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285577,
  "host_pid": "9e6742732c60:1",
  "hash": "2eb2d369aeb66459cfa18e4f6e40385a33493166c3ebda35d27c99d49690924c",
  "cid": "QmV12eb2d369aeb66459cfa18e4f6e40385a33493166",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285577,
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
      "evaluated_at": 1760285577
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
  "sig": "70a28ff3f8e4280ef0885d845a95ca701e54ea66cf50dd7d9bcec8f1b9aaf503"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 24862246, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}