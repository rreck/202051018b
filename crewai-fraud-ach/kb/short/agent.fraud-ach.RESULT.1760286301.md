```json
{
  "id": "cfa00be1e7d94065",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286301,
  "host_pid": "9e6742732c60:1",
  "hash": "6471fe4de02db233fc53b404758003167f2320e4bccd0b4d60e11a4774e81fef",
  "cid": "QmV16471fe4de02db233fc53b404758003167f2320e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286301,
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
      "evaluated_at": 1760286301
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
  "sig": "718517626b14d662a1d9b4e2dea8f3c428db8e7e59d50917d983bf24494470e7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240775358
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': 'b90602c7b9596cb3'}}}