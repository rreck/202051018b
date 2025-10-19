```json
{
  "id": "408ee85818495830",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285102,
  "host_pid": "9e6742732c60:1",
  "hash": "2a9be7fd7525f153e6051494f3e1d93f7825a88e6afa458cc73b4cc28210ec14",
  "cid": "QmV12a9be7fd7525f153e6051494f3e1d93f7825a88e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285102,
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
      "evaluated_at": 1760285102
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
  "sig": "2e2c91ab23633ce9609c5fd6b1ba1a880519348267ba6cf06ad34a1e2428f7ae"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}