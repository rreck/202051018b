```json
{
  "id": "eb920cb5403a63b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288035,
  "host_pid": "9e6742732c60:1",
  "hash": "74d51573a055747a72a2c3761bb10361bb70f3f415e50def034db6ad09b2e8a3",
  "cid": "QmV174d51573a055747a72a2c3761bb10361bb70f3f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288035,
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
      "evaluated_at": 1760288035
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
  "sig": "102b8f58ced78135f7bb3b985e190fa6d355bc6e6949df67328807db9ca7a0af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 21645920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}