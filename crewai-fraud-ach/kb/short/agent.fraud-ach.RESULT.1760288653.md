```json
{
  "id": "a52352046477d49b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288653,
  "host_pid": "9e6742732c60:1",
  "hash": "9f203d049ca90dee7f2315b8b64725db06743456a8dea78fd564a6f929d7e14b",
  "cid": "QmV19f203d049ca90dee7f2315b8b64725db06743456",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288653,
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
      "evaluated_at": 1760288653
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
  "sig": "ebb6f97cc144003b8484ef4705d60c97e7d4f3779d56f43203e7099a40519b22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 34602600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}aly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.06, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7854285}}}