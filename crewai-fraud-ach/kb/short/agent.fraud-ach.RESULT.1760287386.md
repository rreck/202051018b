```json
{
  "id": "71b95c218baa50c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287386,
  "host_pid": "9e6742732c60:1",
  "hash": "4e6ade2939a63512926284993f53b8581e899dd875ca280479388114ce31a0d8",
  "cid": "QmV14e6ade2939a63512926284993f53b8581e899dd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287386,
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
      "evaluated_at": 1760287386
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
  "sig": "feb90d7359143711f29d51e04324eebd7a02e121abedd0c5b1144237d81c7ed2"
}
```

Fraud detected: duplicate_transaction (score: 75)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 66, 'details': {'transaction_count': 58, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}