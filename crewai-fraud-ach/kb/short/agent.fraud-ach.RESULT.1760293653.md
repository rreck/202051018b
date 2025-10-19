```json
{
  "id": "a97c7d1d3aa41a12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293653,
  "host_pid": "9e6742732c60:1",
  "hash": "a354eb03a21afa525837fbdcdb475e01320e342554fd95e8bca2f2a6eb113f76",
  "cid": "QmV1a354eb03a21afa525837fbdcdb475e01320e3425",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293653,
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
      "evaluated_at": 1760293653
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
  "sig": "1495160413ffaed355b144e96a49315d903826cd180bf90a8b966ffc7acd8aca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465206903
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 103405100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'cc8a6efa32cdbdd1'}}}