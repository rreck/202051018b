```json
{
  "id": "bcd909a450012ec7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286850,
  "host_pid": "9e6742732c60:1",
  "hash": "0ada9879bc64f38509a52790ad0085d4d56c08bd6f57bc1df01dce20d146ee14",
  "cid": "QmV10ada9879bc64f38509a52790ad0085d4d56c08bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286850,
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
      "evaluated_at": 1760286850
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
  "sig": "d29d394d512f952d5b6a57fa52efd415792f57369b17649a9d8088d5d33bf32c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000246259253
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}