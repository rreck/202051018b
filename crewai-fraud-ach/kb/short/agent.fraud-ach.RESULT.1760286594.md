```json
{
  "id": "423277bc08bd997c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286594,
  "host_pid": "9e6742732c60:1",
  "hash": "a8c41e5fd926b0a32734e59889d76adb1ffb54a0117726531b5bbafae6ce5336",
  "cid": "QmV1a8c41e5fd926b0a32734e59889d76adb1ffb54a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286594,
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
      "evaluated_at": 1760286594
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
  "sig": "46fb3036740260e624ef118208f7867530158f1ded30a003950c6d1de6512c43"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027607406
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}