```json
{
  "id": "40df977a31c52bf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289582,
  "host_pid": "9e6742732c60:1",
  "hash": "2ceb3bdc942f34275e2a6a88771757f8d7a9c8220d21202e807a8a119581f4f4",
  "cid": "QmV12ceb3bdc942f34275e2a6a88771757f8d7a9c822",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289582,
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
      "evaluated_at": 1760289582
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
  "sig": "2f4b36a3d63122286718238344b681314f711073f763ddfa45b76398f76d8fcb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 59019567, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}