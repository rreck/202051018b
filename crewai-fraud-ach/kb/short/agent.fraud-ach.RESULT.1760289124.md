```json
{
  "id": "3d0c7c0ad88ac195",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289124,
  "host_pid": "9e6742732c60:1",
  "hash": "2b75e1582999398dabbc7824b6e16210ae22b72898646234512e96bd9cd43097",
  "cid": "QmV12b75e1582999398dabbc7824b6e16210ae22b728",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289124,
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
      "evaluated_at": 1760289124
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
  "sig": "49b825b0bcdf8889c76ab516029e429333a2e7c9ca5103bd44e9a1b7cb236b10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248019681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 52436808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'd399d5f74d941af5'}}}