```json
{
  "id": "c07f4318022abbec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286593,
  "host_pid": "9e6742732c60:1",
  "hash": "eb6ab9f7d4813313f70be3c59dffcd6d8245991a608e36909b0c60c0fd177faf",
  "cid": "QmV1eb6ab9f7d4813313f70be3c59dffcd6d8245991a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286593,
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
      "evaluated_at": 1760286593
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
  "sig": "a7d8f4c98cc3d9651a7fe1a7dfce0c2684420e2bc42f270e9dab1d3ebd90a470"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000025198728
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}