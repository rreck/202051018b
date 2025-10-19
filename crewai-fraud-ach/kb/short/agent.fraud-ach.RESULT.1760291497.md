```json
{
  "id": "e8ad34c258e86d5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291497,
  "host_pid": "9e6742732c60:1",
  "hash": "266bdf5de7bf3ea9e83a1aa0db80adcf36f36c3e62a17131abf43283b8a0ba4e",
  "cid": "QmV1266bdf5de7bf3ea9e83a1aa0db80adcf36f36c3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291497,
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
      "evaluated_at": 1760291497
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
  "sig": "a584633bc836e36dc6f0b215449a7ccb6163186ea35e0485f05fdb8e612214d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 40831824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}