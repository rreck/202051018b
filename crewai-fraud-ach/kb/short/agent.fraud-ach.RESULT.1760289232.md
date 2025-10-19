```json
{
  "id": "b50c29f6eea07fc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289232,
  "host_pid": "9e6742732c60:1",
  "hash": "91c8f98b2f2fa5abf6efa9d2de47e384c02082ed7908d72949d8c39f485e6033",
  "cid": "QmV191c8f98b2f2fa5abf6efa9d2de47e384c02082ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289232,
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
      "evaluated_at": 1760289232
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
  "sig": "c3f9a44fc3d171064eef0c43cee36319629eb3f128daa202685806cbb26862f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271105789
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 31718934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': 'b50c8d05dbdb14ee'}}}