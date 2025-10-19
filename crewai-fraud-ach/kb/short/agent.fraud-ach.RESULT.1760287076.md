```json
{
  "id": "4ad61b8b995fe6de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287076,
  "host_pid": "9e6742732c60:1",
  "hash": "5ec37493ded95d7855adcc6d2ca74a845e0085771585f114ff2cf39144443f40",
  "cid": "QmV15ec37493ded95d7855adcc6d2ca74a845e008577",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287076,
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
      "evaluated_at": 1760287076
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "24928b9f2195ec41ebf92e9f8961a2dfec5f3f46aa90fb908bbb0982ce71be6f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10036991, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}