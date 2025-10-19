```json
{
  "id": "58053767fc4ca1bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290265,
  "host_pid": "9e6742732c60:1",
  "hash": "9af016860a3a9123a68efebafd45b8d76538c4f227c5ecc0b424c559a6505222",
  "cid": "QmV19af016860a3a9123a68efebafd45b8d76538c4f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290265,
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
      "evaluated_at": 1760290265
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
  "sig": "a54ed9682df4a195b228ca37fcd1f311301c5052e64ce7b5da78c310b31fabae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 32017946, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}