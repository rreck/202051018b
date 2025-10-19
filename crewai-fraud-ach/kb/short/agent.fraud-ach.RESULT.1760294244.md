```json
{
  "id": "074830cc3a1576fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294244,
  "host_pid": "9e6742732c60:1",
  "hash": "064899c6db207c1199d8a3cf04c1ee2238301654767833430509a0d058c32bfd",
  "cid": "QmV1064899c6db207c1199d8a3cf04c1ee2238301654",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294244,
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
      "evaluated_at": 1760294244
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
  "sig": "753b18c7bb0a213797f2748c0216d8f45a0e460237756ec908df28a603103a60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464550835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 43812288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '50cb0ee46794e046'}}}