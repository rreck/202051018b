```json
{
  "id": "526bcfd571fcd2f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291708,
  "host_pid": "9e6742732c60:1",
  "hash": "2d4f0f44e9913c564f3977b4aaeeb71f6a9ce4f7dc9419c1e970aee63eb9b633",
  "cid": "QmV12d4f0f44e9913c564f3977b4aaeeb71f6a9ce4f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291708,
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
      "evaluated_at": 1760291708
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
  "sig": "659092b528769d66fd48f0fe3270e758e44176067ead8689c43cf81c1a10d4c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031291734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 61643894, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}