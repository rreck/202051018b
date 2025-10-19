```json
{
  "id": "8d95cbd8b17be638",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294196,
  "host_pid": "9e6742732c60:1",
  "hash": "054d5d2e024bff5378a58ec4e28d23ee1b5d1e862dcbfce0e92925e03b0fca94",
  "cid": "QmV1054d5d2e024bff5378a58ec4e28d23ee1b5d1e86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294196,
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
      "evaluated_at": 1760294196
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
  "sig": "408a3cd2a1a5ca8e46fd84b024cd4209e23e038c926ead3f7304f9e3d1d82d19"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 53685996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}