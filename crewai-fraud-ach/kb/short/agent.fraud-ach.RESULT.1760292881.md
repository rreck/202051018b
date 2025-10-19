```json
{
  "id": "206b637dbcc25d94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292881,
  "host_pid": "9e6742732c60:1",
  "hash": "0869d2512546f270ca941b70dc3076f557559fd6f14a827074ff458f1babbc15",
  "cid": "QmV10869d2512546f270ca941b70dc3076f557559fd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292881,
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
      "evaluated_at": 1760292881
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
  "sig": "0be54af2e808a2457bb30ba347a971327b13d097e9b00fb3012cae87f1dd6091"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159610548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 67485105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '505487b98e445d12'}}}maly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6888614}}}