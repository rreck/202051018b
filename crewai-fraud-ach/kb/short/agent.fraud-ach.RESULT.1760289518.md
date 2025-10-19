```json
{
  "id": "a437d079f1411d65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289518,
  "host_pid": "9e6742732c60:1",
  "hash": "19a237b59a14acb90e6ec32cb94568b993a1cbcaf8a4b7d4b183a6b93874401c",
  "cid": "QmV119a237b59a14acb90e6ec32cb94568b993a1cbca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289518,
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
      "evaluated_at": 1760289518
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
  "sig": "12e95c6c89ed58abf61911b93c27baf561f340a9d2d18eca614b8fe89b76cf75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 30181750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}