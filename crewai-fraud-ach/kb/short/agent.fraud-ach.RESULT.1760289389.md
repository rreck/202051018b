```json
{
  "id": "ca668248dd346fd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289389,
  "host_pid": "9e6742732c60:1",
  "hash": "18e37135306a015d2c0ee4469b5c002ffbf43ec0654b63682e43c6300ebcf469",
  "cid": "QmV118e37135306a015d2c0ee4469b5c002ffbf43ec0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289389,
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
      "evaluated_at": 1760289389
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
  "sig": "867dcbdbdf3808f2623a0ff35e8fe988e3b6cdf9a37441cf0cc6eea2a0d395a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030152104
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 35490654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': 'f9baa0480a932ad2'}}}aly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7365830}}}