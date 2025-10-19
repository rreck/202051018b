```json
{
  "id": "cb70d35b6664a299",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293566,
  "host_pid": "9e6742732c60:1",
  "hash": "ca94e2b8fab87a92cd656bc9c59e5be950becf796bb8a86f4cfc153fc12c7ef9",
  "cid": "QmV1ca94e2b8fab87a92cd656bc9c59e5be950becf79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293566,
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
      "evaluated_at": 1760293566
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
  "sig": "18e867aa18aa67e9a5d88e5c980e6aa4e5e1ff8f0455c5ed6376f56f713848f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155063461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 69625608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}