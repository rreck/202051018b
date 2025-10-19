```json
{
  "id": "b43ca2a3908d1b16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292877,
  "host_pid": "9e6742732c60:1",
  "hash": "4c12aa557d2924f48c271a662fe34c2111f8c777194a1c44535d54c0d0dca9f1",
  "cid": "QmV14c12aa557d2924f48c271a662fe34c2111f8c777",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292877,
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
      "evaluated_at": 1760292877
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
  "sig": "0e08385c7ed00df91a27cc035a904b19b05da616b7da2ed20885bf34335b2333"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 111000023893131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 2032248582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '5255bec7f5e0b39d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.18, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9817626}}}