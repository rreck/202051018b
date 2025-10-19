```json
{
  "id": "9eaff59cd9a79f0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286665,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce5701b2e5da075008fd18199741e9c588ece22f9947e71d5214ade5e87ae3f",
  "cid": "QmV18ce5701b2e5da075008fd18199741e9c588ece22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286665,
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
      "evaluated_at": 1760286665
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
  "sig": "d10497d06e60a4bfe0608ba014186586c9375d7e4b41a0e9a2f4b9d5e8d9655c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240775358
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': 'b90602c7b9596cb3'}}}