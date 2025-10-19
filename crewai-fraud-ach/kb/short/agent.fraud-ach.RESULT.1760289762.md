```json
{
  "id": "9bf268de574a645b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289762,
  "host_pid": "9e6742732c60:1",
  "hash": "da1d701941052ccb2c75fc4cdbd2ccb84c960c2d79f8726ccd75fd2b5955d618",
  "cid": "QmV1da1d701941052ccb2c75fc4cdbd2ccb84c960c2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289762,
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
      "evaluated_at": 1760289762
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
  "sig": "1e9a261dc51a654f48b23be57234195be21bd9a85a5ab91311f86a2314ce0b28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 62363400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}