```json
{
  "id": "487677d799e9157e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286153,
  "host_pid": "9e6742732c60:1",
  "hash": "08f9f4f48061f55a432ceca947d556bbcafe00c6a8f728298ff346b5c29fd1f3",
  "cid": "QmV108f9f4f48061f55a432ceca947d556bbcafe00c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286153,
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
      "evaluated_at": 1760286153
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
  "sig": "7af996e88db15f28671c901cec0bcd68b038b7dd6cb9ed152a0fa59ecda55398"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100273039049
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '71e11df02cc7494b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}