```json
{
  "id": "459f89c1dae0cf3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293324,
  "host_pid": "9e6742732c60:1",
  "hash": "fa5e4e02b476d243bddb64fe19d872c9a329fbe84a8da185bda6abeaba33db07",
  "cid": "QmV1fa5e4e02b476d243bddb64fe19d872c9a329fbe8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293324,
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
      "evaluated_at": 1760293325
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
  "sig": "cd6f058e248322a2e987019b79b20cc2873b5994fc8de4d13b1c5c695b71f996"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594957329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 107523504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '2b2bf7f9f831f062'}}}