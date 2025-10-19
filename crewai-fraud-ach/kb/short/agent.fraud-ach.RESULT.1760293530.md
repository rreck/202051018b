```json
{
  "id": "f864cbb7917f60aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293530,
  "host_pid": "9e6742732c60:1",
  "hash": "ac5961e944fc1652290927ec5d0d8b72eaf9318e14f4f2ba3aa3e4aa5f3e6132",
  "cid": "QmV1ac5961e944fc1652290927ec5d0d8b72eaf9318e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293530,
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
      "evaluated_at": 1760293530
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
  "sig": "07a936a532f8266e2c91956c62b3abfc0d2383536703d1790ec0a4aef77cbc7c"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 2051123140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.9, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9323287}}}