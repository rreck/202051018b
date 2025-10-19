```json
{
  "id": "721a756b74a09d6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286031,
  "host_pid": "9e6742732c60:1",
  "hash": "520c114756448d66569b4a16821e1bc335ae77e33bc8a44693248c7d6d764d0e",
  "cid": "QmV1520c114756448d66569b4a16821e1bc335ae77e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286031,
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
      "evaluated_at": 1760286031
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
  "sig": "62a0a5333fc4ed0e840b913e86b96460370382cf99529cf1ea0364c1c73e03d5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466771941
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': 'aa929aac6878f78f'}}}