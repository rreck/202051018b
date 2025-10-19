```json
{
  "id": "346ed1f6f650c244",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287166,
  "host_pid": "9e6742732c60:1",
  "hash": "7b0a0f3215960093586f674c4d5536afb315095041fcfc65b38caddaa0b6f8e6",
  "cid": "QmV17b0a0f3215960093586f674c4d5536afb3150950",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287166,
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
      "evaluated_at": 1760287166
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c43a57aa967697bcf0434a7161b541ef9696bbfbfd549a5cf1d5b58fa4d0afbc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20377200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}