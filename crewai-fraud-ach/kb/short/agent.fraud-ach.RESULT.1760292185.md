```json
{
  "id": "2b475369d321cb3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292185,
  "host_pid": "9e6742732c60:1",
  "hash": "8b0bccbf984fef774c66b8ddf794ccf634bacf8924e9e76f242d4f8937148f19",
  "cid": "QmV18b0bccbf984fef774c66b8ddf794ccf634bacf89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292185,
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
      "evaluated_at": 1760292185
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
  "sig": "6d78c683c85144a49f7eacecd578c9d0cd2cab1daa1528cb0073922312035b70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274521172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 20467584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': 'cfb56b896e519b42'}}}