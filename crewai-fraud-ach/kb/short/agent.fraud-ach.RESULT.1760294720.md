```json
{
  "id": "f208ddb5541a4f80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294720,
  "host_pid": "9e6742732c60:1",
  "hash": "f86b81dbc3d6b93ed28df95ab4124bbee626a2bc3af483dc0fabd65f51f881a8",
  "cid": "QmV1f86b81dbc3d6b93ed28df95ab4124bbee626a2bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294720,
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
      "evaluated_at": 1760294720
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
  "sig": "685790e4fc0b0c3c4c276003c1aa275d1832919f22a34c16f58562966f4f9d3f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150565846
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 120520710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': 'c006c1a99d006ad8'}}}