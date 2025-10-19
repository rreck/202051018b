```json
{
  "id": "874ab99e4d0ff5cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286807,
  "host_pid": "9e6742732c60:1",
  "hash": "a7e60eb69e4983268367b57ab7597aa01e595194053de00d4dfb4b7a5a10ea13",
  "cid": "QmV1a7e60eb69e4983268367b57ab7597aa01e595194",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286807,
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
      "evaluated_at": 1760286807
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
  "sig": "8abdf189d22657a98fd092b42175e4cf7ac0dfcb6731a520cf12de12d7944a27"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241612576
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': 'a67f7546b45b9310'}}}