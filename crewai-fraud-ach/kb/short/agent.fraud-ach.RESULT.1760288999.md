```json
{
  "id": "5a22f9ec6e8b1800",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288999,
  "host_pid": "9e6742732c60:1",
  "hash": "aca72b7eb506837c2f67bb60372042d31fad2ddf8df3b7fdd718ac3a4800edbc",
  "cid": "QmV1aca72b7eb506837c2f67bb60372042d31fad2ddf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288999,
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
      "evaluated_at": 1760288999
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "5c58d1cec0f02303704fcc6852109b75a59a1fe97ca4055fcb3001bd9693d8a3"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 897562050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 82, 'details': {'zscore': 4.23, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8159655}}}