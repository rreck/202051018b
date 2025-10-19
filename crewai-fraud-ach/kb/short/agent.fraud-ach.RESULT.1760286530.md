```json
{
  "id": "a77a904739402585",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286530,
  "host_pid": "9e6742732c60:1",
  "hash": "8e563df5734fda56af6f47f3845c019540a3034bb451bf2da607f6f542164ba9",
  "cid": "QmV18e563df5734fda56af6f47f3845c019540a3034b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286530,
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
      "evaluated_at": 1760286530
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
  "sig": "cab2b387cc8ca8757bac0fb76ffc4eb3d6ad9ea0e42e1b027dbcf244863f4139"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100272414433
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285764, 'matching_hash': 'f489e4bd64364941'}}}