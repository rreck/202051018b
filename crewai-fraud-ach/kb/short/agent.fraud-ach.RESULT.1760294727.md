```json
{
  "id": "dbc330cec5117dda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294727,
  "host_pid": "9e6742732c60:1",
  "hash": "13db9207b65470eef3fa93fe77c559bd79566be87478d3f0a4047619e443465e",
  "cid": "QmV113db9207b65470eef3fa93fe77c559bd79566be8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294727,
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
      "evaluated_at": 1760294727
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
  "sig": "8c6cd55f0db8438055192ef89b4a05c181060bdebd039ef1a3c57b452230eeaf"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 031201462394531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 1855808010, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '046e1c7f2d74b138'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.94, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7637070}}}