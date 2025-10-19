```json
{
  "id": "37126e479c5af034",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289511,
  "host_pid": "9e6742732c60:1",
  "hash": "7bde71ca7c732e542bb2fde3cda2ce350d2c2fdb4b62551675b75702a2364240",
  "cid": "QmV17bde71ca7c732e542bb2fde3cda2ce350d2c2fdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289511,
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
      "evaluated_at": 1760289511
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
  "sig": "a1da21df90226d9fd36178954cc471b1941a8f246351cdfd7b8fcb75f53dbc5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 53865875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}