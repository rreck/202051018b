```json
{
  "id": "dd1a33f4144acd72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289260,
  "host_pid": "9e6742732c60:1",
  "hash": "2775d7bb79463484518c35eaba3335b93f4fa70f7bf83e5b0a32bebe579efb78",
  "cid": "QmV12775d7bb79463484518c35eaba3335b93f4fa70f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289260,
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
      "evaluated_at": 1760289260
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
  "sig": "04ef700a853ede293273a4d5f317d8d051653667c152a7bd9f5fae6ece566f59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029230021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 38642994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': 'f06e706b59004f2f'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}