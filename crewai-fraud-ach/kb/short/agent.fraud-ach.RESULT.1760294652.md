```json
{
  "id": "41377f4c30ebba8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294652,
  "host_pid": "9e6742732c60:1",
  "hash": "b45f473861f632c8105cc16a775235e052c58e96b0c3664b28144db4475bfabe",
  "cid": "QmV1b45f473861f632c8105cc16a775235e052c58e96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294652,
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
      "evaluated_at": 1760294652
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
  "sig": "73c9666ebc58f0d93694e2cf8242c8ab6b77b98e0adcef6f90d19d9846d246b0"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 021000028707079
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 1657670234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '67ae9df98d5fdee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.49, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6849877}}}