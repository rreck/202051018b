```json
{
  "id": "1d000f6f57c84ce8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289439,
  "host_pid": "9e6742732c60:1",
  "hash": "382b2ebd86af109ee7798be17ff8fa2ff49af49900c2debeb568657bd16356a9",
  "cid": "QmV1382b2ebd86af109ee7798be17ff8fa2ff49af499",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289439,
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
      "evaluated_at": 1760289439
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
  "sig": "fcfe7195820c27973062290944c0e0e99853531be0c0fc5ff5361d2dddf0cbb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243177921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 42394410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}