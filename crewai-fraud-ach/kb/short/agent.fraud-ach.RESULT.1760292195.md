```json
{
  "id": "d0f904c591aa452e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292195,
  "host_pid": "9e6742732c60:1",
  "hash": "c2ef9ee47d68c907a684d33507b1bbeeca7084b9f084e6771c63a48684ebb5c3",
  "cid": "QmV1c2ef9ee47d68c907a684d33507b1bbeeca7084b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292195,
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
      "evaluated_at": 1760292195
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
  "sig": "5a43a5bc22009b93068780824a614fd3af597ca5c9334df3afc14e0034d9fca1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594714846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 268, 'threshold': 50, 'total_amount': 132940328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 267, 'first_seen': 1760284979, 'matching_hash': 'bc3982de93079c96'}}}