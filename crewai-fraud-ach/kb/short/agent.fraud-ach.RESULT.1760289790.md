```json
{
  "id": "cce0f04501341383",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289790,
  "host_pid": "9e6742732c60:1",
  "hash": "6478f1e2d2bb5d3fc98be8d9393f09b61d35a79acb3e0e1a705092b0437960b0",
  "cid": "QmV16478f1e2d2bb5d3fc98be8d9393f09b61d35a79a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289790,
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
      "evaluated_at": 1760289790
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
  "sig": "a4ec723419ab203ee0e952a01c6788e757f5b8048281d8015c953c78a77cdcba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461912165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 46698827, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': 'd770463353c2594b'}}}