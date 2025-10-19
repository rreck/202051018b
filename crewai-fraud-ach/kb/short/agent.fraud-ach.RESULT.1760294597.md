```json
{
  "id": "01f76756c56e6dd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294597,
  "host_pid": "9e6742732c60:1",
  "hash": "0f0075693c2bc1882fa16d6fbed18f90336d25b43a5da942faa8b8c72a5a4589",
  "cid": "QmV10f0075693c2bc1882fa16d6fbed18f90336d25b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294597,
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
      "evaluated_at": 1760294597
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
  "sig": "af1b5cfd3332df9345ec1163dec6dd015e4654ed9940aca8485601b3890b32d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 70536603, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}