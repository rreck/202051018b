```json
{
  "id": "3567eea0743b8cfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289459,
  "host_pid": "9e6742732c60:1",
  "hash": "ceae5b7178cb76bf3edec78e48b4fb1688da99b9747eb1015247e2e9d351fcce",
  "cid": "QmV1ceae5b7178cb76bf3edec78e48b4fb1688da99b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289459,
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
      "evaluated_at": 1760289459
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
  "sig": "697cd83e96fad5337cbcf0a5e7ccd3b9ff2cb9f1fcce1923257e25c71ce1631c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158127705
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 36422892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': 'c9228fea95a929fd'}}}