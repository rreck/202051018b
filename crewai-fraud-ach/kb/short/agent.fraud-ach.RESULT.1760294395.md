```json
{
  "id": "e7cb4ada983b862b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294395,
  "host_pid": "9e6742732c60:1",
  "hash": "e978ae15220c6d23fa4315c5d1c74039fe36adcd53ad32f64f713648f614a47a",
  "cid": "QmV1e978ae15220c6d23fa4315c5d1c74039fe36adcd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294395,
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
      "evaluated_at": 1760294395
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
  "sig": "7c5f1b0d08c7d56d73e3f68fc5c7009ff608afe12936eae1fe57eeb90674dead"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243890645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 43156515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}