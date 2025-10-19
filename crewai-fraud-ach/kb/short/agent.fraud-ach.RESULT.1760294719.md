```json
{
  "id": "da36193a9a32865e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294719,
  "host_pid": "9e6742732c60:1",
  "hash": "d93de54f0e57feda20e60bf1259713c3ff20dd52f9aaee2ec59ff844399a8d12",
  "cid": "QmV1d93de54f0e57feda20e60bf1259713c3ff20dd52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294719,
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
      "evaluated_at": 1760294719
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
  "sig": "db5e007f011e22c6fbe8b478f49694af5465339d0589c1f2c00effaac98c6361"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 319, 'threshold': 50, 'total_amount': 84234502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 318, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}