```json
{
  "id": "632df28760166140",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289854,
  "host_pid": "9e6742732c60:1",
  "hash": "ee1a217435c60feda61e096ee9ca7e1edf729c5726c4d8fa40aa0dbce52e021b",
  "cid": "QmV1ee1a217435c60feda61e096ee9ca7e1edf729c57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289854,
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
      "evaluated_at": 1760289854
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
  "sig": "908e809b6a924ee95ee1e9212b116e75c1ab1c68de3a0319e279f5e28f1ed168"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154786749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 59285385, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '09892425b2f11015'}}}