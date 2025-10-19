```json
{
  "id": "1e489fae56777d8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290058,
  "host_pid": "9e6742732c60:1",
  "hash": "f3c6fd0fa2a428528386765d904a0d37e6ff66c65ad8cc6a112fc9d1589a1450",
  "cid": "QmV1f3c6fd0fa2a428528386765d904a0d37e6ff66c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290058,
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
      "evaluated_at": 1760290058
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
  "sig": "45da5b46edf98f5b2ce674e1b242d5f3f25475d0187f63b522bf31e727aea261"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 63678160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}