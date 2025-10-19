```json
{
  "id": "e1306d8104aea018",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292299,
  "host_pid": "9e6742732c60:1",
  "hash": "f2a7d7894009a7e30a1aaf50252ca26d70f5ea7c6ecf479bc5663c7a41efc4ac",
  "cid": "QmV1f2a7d7894009a7e30a1aaf50252ca26d70f5ea7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292299,
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
      "evaluated_at": 1760292299
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
  "sig": "26eb8468e1767068de574cd06fef3f8163052300cd8ddad8ae6b7c24bc4efbc1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156006729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': 'e8898c854a66ef00'}}}