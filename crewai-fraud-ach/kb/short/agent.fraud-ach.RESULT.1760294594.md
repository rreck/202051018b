```json
{
  "id": "b0d2262976c8da3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294594,
  "host_pid": "9e6742732c60:1",
  "hash": "6f2b2ba173681a143aade7d0a06bca193cc1437269e526a92df0e7f15ee3ffe2",
  "cid": "QmV16f2b2ba173681a143aade7d0a06bca193cc14372",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294594,
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
      "evaluated_at": 1760294594
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
  "sig": "ec57915849b0b09397d7bc0da594dfbba8bf25fd8e964b5e477e7f70c1060384"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201465065641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 1484916439, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'c71bd5f7fa32abe1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6161479}}}}