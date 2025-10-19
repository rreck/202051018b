```json
{
  "id": "f59f34c0f8027f0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292460,
  "host_pid": "9e6742732c60:1",
  "hash": "fcd0042f7b6eae4fdadbecaed47e085a23468ea223ad625edec2e734b6d38bd4",
  "cid": "QmV1fcd0042f7b6eae4fdadbecaed47e085a23468ea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292460,
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
      "evaluated_at": 1760292460
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
  "sig": "eb6b6c1062bad43da9d5cdb6f4585d8ae480840708a7d91f1fe7bf5dd23a7f92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245035140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 80196930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'af29b59576821758'}}}