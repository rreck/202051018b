```json
{
  "id": "2e8a148fa695ed6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287101,
  "host_pid": "9e6742732c60:1",
  "hash": "95114935403f61d2b5f736dc31b8e4e2132468bf4ff5a08b65bd2cf12674f421",
  "cid": "QmV195114935403f61d2b5f736dc31b8e4e2132468bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287101,
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
      "evaluated_at": 1760287101
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
  "sig": "64631f9db7447fbc36036899ff1e6d04a5d2980fe20041554e56d1c7f050b339"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022841229
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}