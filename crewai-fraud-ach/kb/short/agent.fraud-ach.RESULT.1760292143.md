```json
{
  "id": "9c6ced45cbd96db5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292143,
  "host_pid": "9e6742732c60:1",
  "hash": "e5e493c997f899d77d58b9448aac966d4b8b912a48d7c2567cd0f6fa4c5176b1",
  "cid": "QmV1e5e493c997f899d77d58b9448aac966d4b8b912a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292143,
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
      "evaluated_at": 1760292143
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
  "sig": "a1c2921be35c4453d50c01d91a24c70473ba18d557b78a3485cd83119d1e99c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 69370818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}