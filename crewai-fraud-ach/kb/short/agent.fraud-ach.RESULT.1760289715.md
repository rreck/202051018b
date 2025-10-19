```json
{
  "id": "c6d4ccfea3a68b4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289715,
  "host_pid": "9e6742732c60:1",
  "hash": "602cb74727371ec966c23245d60ef76a16cc9bc172b7820b6fcf6a110099237d",
  "cid": "QmV1602cb74727371ec966c23245d60ef76a16cc9bc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289715,
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
      "evaluated_at": 1760289715
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
  "sig": "08b950b66c8758d9b31bcdb569e1507b1708cedd9b5c89dfc42cafc9bd611b49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273957576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 59317062, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '30cc5398d3c09035'}}}maly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9546317}}}