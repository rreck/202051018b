```json
{
  "id": "9eb3e0c6d7fece21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291881,
  "host_pid": "9e6742732c60:1",
  "hash": "8b0e37993b2048fa63f6aec8de7936c777f35afb36e6deff36c7bfd0414a4cf6",
  "cid": "QmV18b0e37993b2048fa63f6aec8de7936c777f35afb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291881,
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
      "evaluated_at": 1760291881
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
  "sig": "07e3fc1068610fe566dcdd487c5e1e44bd3082f8b9d22275180c818918ebd300"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 261, 'threshold': 50, 'total_amount': 99063594, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 260, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}