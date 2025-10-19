```json
{
  "id": "22b015272b4f1b6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760284990,
  "host_pid": "9e6742732c60:1",
  "hash": "dce92d2b60307209ce55b85df3875f1ad5e644b9a29f239df991e0b1248e1a39",
  "cid": "QmV1dce92d2b60307209ce55b85df3875f1ad5e644b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760284990,
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
      "evaluated_at": 1760284990
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
  "sig": "89c2ac0376dafa307e4780bad09ba79e0918d1714fcbf870ec803c951359d790"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}