```json
{
  "id": "4edd7c9c834b4919",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288241,
  "host_pid": "9e6742732c60:1",
  "hash": "38a774424a810986ffa2c273fdc7deb98e0738624bb9d64366e09e9d20d602f4",
  "cid": "QmV138a774424a810986ffa2c273fdc7deb98e073862",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288241,
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
      "evaluated_at": 1760288241
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
  "sig": "d819b4b0154f66d6b49393c23fafabd32d5677e2bf04f766c456b3784e13d73c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599908299
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 38391882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': '494601c315920761'}}}}}y': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6276049}}}