```json
{
  "id": "41744e24d3e3eaf5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291828,
  "host_pid": "9e6742732c60:1",
  "hash": "93ba3e6246a201932e7f89c9ce153e0091f8b084955f2801c2bcda0319d9a357",
  "cid": "QmV193ba3e6246a201932e7f89c9ce153e0091f8b084",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291828,
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
      "evaluated_at": 1760291828
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
  "sig": "b49ae8a485a8b494bcaffae3465c4c25596bf0e1063fd948d23fe72d35189d9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023390591
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 57592736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': '65b6a0d7e3017724'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}