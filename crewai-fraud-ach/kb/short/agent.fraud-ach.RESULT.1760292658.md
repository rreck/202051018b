```json
{
  "id": "662cccc92044d5cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292658,
  "host_pid": "9e6742732c60:1",
  "hash": "b679a5b323a5a1ad1f7ea7b78bb6392c0261c91e77e84254ee29aa43f1a9ec1a",
  "cid": "QmV1b679a5b323a5a1ad1f7ea7b78bb6392c0261c91e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292658,
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
      "evaluated_at": 1760292658
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
  "sig": "3dfa0f0ad9a37ca298a8bd78ea8af9ac9a06cb200d2de6babb67c39f0c4c8e55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241784115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 90890102, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'd8ced4219e23835b'}}}