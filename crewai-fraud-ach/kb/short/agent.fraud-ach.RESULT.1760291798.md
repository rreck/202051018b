```json
{
  "id": "bb5671355b166cba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291798,
  "host_pid": "9e6742732c60:1",
  "hash": "60c85a19d81d49dac220f626ec1c9ffbc5aca4f7cb7f84391c2ac147f4c476e9",
  "cid": "QmV160c85a19d81d49dac220f626ec1c9ffbc5aca4f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291798,
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
      "evaluated_at": 1760291798
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
  "sig": "49a44aa4ee91b4d26ebc21e57912387acebd86221a4781dd7131358c9995a286"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 72464706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}