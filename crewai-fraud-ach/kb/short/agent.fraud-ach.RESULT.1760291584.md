```json
{
  "id": "c6f290b8cbbddc3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291584,
  "host_pid": "9e6742732c60:1",
  "hash": "0b0d6b210746a1f6a8417d5cf7a6a9b087b27f4582248d75135c3752b5092d18",
  "cid": "QmV10b0d6b210746a1f6a8417d5cf7a6a9b087b27f45",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291584,
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
      "evaluated_at": 1760291584
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
  "sig": "252746ee558973a36f6e8537392342c86a575610c71e6f1ad5c0c8f18751cd1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 72181314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}