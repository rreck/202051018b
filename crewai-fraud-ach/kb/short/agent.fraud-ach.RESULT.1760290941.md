```json
{
  "id": "cdaa8ea3b1a4fb80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290941,
  "host_pid": "9e6742732c60:1",
  "hash": "23bfb78354a12edcf7b72d02c50629693097bf97cf799393ba3e05c28cc498e4",
  "cid": "QmV123bfb78354a12edcf7b72d02c50629693097bf97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290941,
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
      "evaluated_at": 1760290941
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
  "sig": "1a3248544fde21cba94fdefee89915dace955b3b9db25c80379cb34c653c4781"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 66343445, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}