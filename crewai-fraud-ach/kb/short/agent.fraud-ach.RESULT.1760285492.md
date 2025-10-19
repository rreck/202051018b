```json
{
  "id": "d348b257aad09f29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285492,
  "host_pid": "9e6742732c60:1",
  "hash": "c56b734f2aa7c2a9c39f1b660b7e03c2eb278424a95abcf8655a52419e9bdb23",
  "cid": "QmV1c56b734f2aa7c2a9c39f1b660b7e03c2eb278424",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285492,
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
      "evaluated_at": 1760285492
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
  "sig": "9d61b51ef851033a2a04a2d0c76ab628a92ff05c76ef354ce2b25a924dce9633"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 21491094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}