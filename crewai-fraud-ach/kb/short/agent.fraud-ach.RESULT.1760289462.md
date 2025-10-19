```json
{
  "id": "3c8f6a6aba8de95f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289462,
  "host_pid": "9e6742732c60:1",
  "hash": "cff7978381e63f40c5e006bb300da82d3a81aff1f478e38b79ca9c586894aa77",
  "cid": "QmV1cff7978381e63f40c5e006bb300da82d3a81aff1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289462,
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
      "evaluated_at": 1760289462
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
  "sig": "b7ba71f7ea677d37c4f299daeb53f933d13918ead2b8c4e2280155a0d6db9d4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 42907224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}