```json
{
  "id": "33c695ba405f75d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286669,
  "host_pid": "9e6742732c60:1",
  "hash": "26c85e183a261a8b42c3561e9eb5362191aef65bed6dba28d20234cb0612aa35",
  "cid": "QmV126c85e183a261a8b42c3561e9eb5362191aef65b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286669,
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
      "evaluated_at": 1760286669
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
  "sig": "a9da6472c04b394917ee1bfe5964c278093c8373779b8fe2f9853329dd40058c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024242004
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': '99660a13145cb677'}}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760284979, 'matching_hash': '6a7cc3d9f67da590'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}