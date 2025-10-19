```json
{
  "id": "61fad4cb4cf8b383",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291479,
  "host_pid": "9e6742732c60:1",
  "hash": "87fad902a9b85ad97d0e8849b09552e2c44a0b95a6f2d47cfce7fbec8d625c4f",
  "cid": "QmV187fad902a9b85ad97d0e8849b09552e2c44a0b95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291479,
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
      "evaluated_at": 1760291479
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
  "sig": "5bf049ac253894e308ab60cae3fe2842be23e08a4d0e4aa33abf93da32574793"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 60900576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}