```json
{
  "id": "5b576953fad194a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285608,
  "host_pid": "9e6742732c60:1",
  "hash": "15c3c90cb058b9e340b8a5d98ab7d6ea51d1534be2cd429b31461c719ee71e9f",
  "cid": "QmV115c3c90cb058b9e340b8a5d98ab7d6ea51d1534b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285608,
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
      "evaluated_at": 1760285608
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
  "sig": "230217c2aff22695aa0a320b0b72122eda9a66568540922860f71d965fb154f6"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 26126428, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}