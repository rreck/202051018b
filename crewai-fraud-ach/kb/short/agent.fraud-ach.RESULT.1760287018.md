```json
{
  "id": "83183f2b55ae82ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287018,
  "host_pid": "9e6742732c60:1",
  "hash": "42a77e11a770936dfbfbc3ee834b7149ad944b6a1b4d562cb7ebb1c8a8b9997e",
  "cid": "QmV142a77e11a770936dfbfbc3ee834b7149ad944b6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287018,
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
      "evaluated_at": 1760287018
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
  "sig": "3e93d391771ade74769d540d197d9c0c48000ae016a6faef46105d46222da205"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201468284841
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}