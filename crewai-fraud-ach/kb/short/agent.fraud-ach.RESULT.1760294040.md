```json
{
  "id": "2dc0736d772f5c6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294040,
  "host_pid": "9e6742732c60:1",
  "hash": "dbc524626e96c1d856999afbdbf37fc869294155be5abb1d4eb37b3bcfcdd833",
  "cid": "QmV1dbc524626e96c1d856999afbdbf37fc869294155",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294040,
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
      "evaluated_at": 1760294040
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
  "sig": "1b275cd433dbee33177e818c6db8daaab60c2e467f1d20dd477d8f27da3e3e8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038907358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 49743250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '4f1b5532b664e41d'}}}