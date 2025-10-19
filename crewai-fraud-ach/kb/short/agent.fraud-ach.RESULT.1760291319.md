```json
{
  "id": "aae0be327e642755",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291319,
  "host_pid": "9e6742732c60:1",
  "hash": "7825fdef78ce9f582a4aad36d42198c0aec67984732ca820a48bf9d5f152c110",
  "cid": "QmV17825fdef78ce9f582a4aad36d42198c0aec67984",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291319,
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
      "evaluated_at": 1760291319
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
  "sig": "638f74b6f770c448a4169fdd767b0c3861d2acff5d753ec6e422fd662640c807"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271259155
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 68043028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '525a45536127a4d2'}}}