```json
{
  "id": "b6bb2402c70abf76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294534,
  "host_pid": "9e6742732c60:1",
  "hash": "2fa659f54f8669d8783231a0e402d373013091a4d1b8b34b4044fb296f9707af",
  "cid": "QmV12fa659f54f8669d8783231a0e402d373013091a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294534,
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
      "evaluated_at": 1760294534
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
  "sig": "f892cd6a461fa387a527799790c1d8d9e1c7d00e4b6998961a2f6154af345485"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000024041930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 1767799200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7365830}}}