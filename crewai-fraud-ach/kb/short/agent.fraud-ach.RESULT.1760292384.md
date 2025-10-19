```json
{
  "id": "511a4b604bc25f98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292384,
  "host_pid": "9e6742732c60:1",
  "hash": "d0fed60227d6af7ee9fd59161b80b27279f127eec90dde14a5b4c7aa5e1c426c",
  "cid": "QmV1d0fed60227d6af7ee9fd59161b80b27279f127ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292384,
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
      "evaluated_at": 1760292384
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
  "sig": "b8286c65d0511cd9360620978f09a3bc676f2e0fc4a6c6d544dfe962df0f8dc8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 89149424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}