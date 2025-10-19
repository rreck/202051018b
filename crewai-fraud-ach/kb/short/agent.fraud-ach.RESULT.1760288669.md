```json
{
  "id": "fa0f1becd06e8522",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288669,
  "host_pid": "9e6742732c60:1",
  "hash": "d54d9138ca655e0750320700a65710b737bdd194b2c1b0b7c4f10aff01e69f08",
  "cid": "QmV1d54d9138ca655e0750320700a65710b737bdd194",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288669,
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
      "evaluated_at": 1760288669
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
  "sig": "c9c4b7acc60b3d31c9ceea4cca57ba759c93e25922ba00544c2de0f02183dc52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246259253
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 11061400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}