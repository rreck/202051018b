```json
{
  "id": "3fb85e08a8825858",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286898,
  "host_pid": "9e6742732c60:1",
  "hash": "b7a15811916db5b35a4c889d5e4e49d7632364e1cd6205d492ab52b832ed23c1",
  "cid": "QmV1b7a15811916db5b35a4c889d5e4e49d7632364e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286898,
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
      "evaluated_at": 1760286898
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
  "sig": "e514645be76204e2386ba212e6becd96c6f102e76ebd8a4c5311567a0f6c3070"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270359022
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': '8c09836a51c1ceac'}}}760284979, 'matching_hash': '00d004b11e9e3015'}}}