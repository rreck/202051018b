```json
{
  "id": "1f674bd2d7fe9308",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285165,
  "host_pid": "9e6742732c60:1",
  "hash": "de18832554e2c2645a19e542df036e08d21e602f1b4a7ef5c7c412d2996c0998",
  "cid": "QmV1de18832554e2c2645a19e542df036e08d21e602f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285165,
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
      "evaluated_at": 1760285165
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
  "sig": "09481ee2da85e85ebdf3e5eda20103e3f557e8660a88d1cdacc75100518ad7b7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}