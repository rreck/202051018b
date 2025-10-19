```json
{
  "id": "6f0c1fed59ee02b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293112,
  "host_pid": "9e6742732c60:1",
  "hash": "02d669cf9a21b8003fe185a01f45ef683fda25524bf2c6ae14db057ac5b98200",
  "cid": "QmV102d669cf9a21b8003fe185a01f45ef683fda2552",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293112,
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
      "evaluated_at": 1760293112
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
  "sig": "d19aefcc109edfc9aaf84d6bccc920ab59d71a3639a55ae63ad16283ef5070a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241612576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 16469008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'a67f7546b45b9310'}}}