```json
{
  "id": "1635e9e5d3cd9039",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288390,
  "host_pid": "9e6742732c60:1",
  "hash": "a556d0cbd66d8404bf3b0a8a623c29d613880f52fb733900d8ebc777ffdc5cc3",
  "cid": "QmV1a556d0cbd66d8404bf3b0a8a623c29d613880f52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288390,
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
      "evaluated_at": 1760288390
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
  "sig": "52c7a8ec010d8568f6a90049725b35d564a3f5de51733c9cba9b76457ef6f26a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021760547
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 23866548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': 'fad63ed6e9f4a51a'}}}