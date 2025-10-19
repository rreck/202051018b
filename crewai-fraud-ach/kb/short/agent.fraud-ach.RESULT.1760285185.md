```json
{
  "id": "58705d406470c628",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285185,
  "host_pid": "9e6742732c60:1",
  "hash": "5b265d3376568d17c32fb2fd2c7da3d5e745a65947e41ce979f66dd6fa1031f8",
  "cid": "QmV15b265d3376568d17c32fb2fd2c7da3d5e745a659",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285185,
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
      "evaluated_at": 1760285185
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
  "sig": "a0a1cd39e4991399d13b4871d7b44fbfa92407e44cb52247692860cb31fc5e5c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}