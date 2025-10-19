```json
{
  "id": "c1cf68e1f805940a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293387,
  "host_pid": "9e6742732c60:1",
  "hash": "7ebcb63142fff191292c40906362c3349e26fbeef9524978eda64146f018b491",
  "cid": "QmV17ebcb63142fff191292c40906362c3349e26fbee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293387,
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
      "evaluated_at": 1760293387
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
  "sig": "f6dac02cc6ce3b0ba14a135fc12b9d40fdeafc43a8ad6b5eea41723c0cb932ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 104196890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}