```json
{
  "id": "db2d40560e5a880b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288814,
  "host_pid": "9e6742732c60:1",
  "hash": "5fef84b01306ef9666170495815bbbd35c1fb14ca687cec2e170cb9f7f6eed6a",
  "cid": "QmV15fef84b01306ef9666170495815bbbd35c1fb14c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288814,
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
      "evaluated_at": 1760288814
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
  "sig": "f3b694ba52f4616d92b44b7852fec57ab3d3fae3a79f266bbeae89db0103559d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468983209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 29970885, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}aly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}