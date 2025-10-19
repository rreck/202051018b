```json
{
  "id": "c6e262061ddad082",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293835,
  "host_pid": "9e6742732c60:1",
  "hash": "8410d52ebdb1c3c4ad29eb747b327b17bb42e4c8f5a0326f483866df36a7b815",
  "cid": "QmV18410d52ebdb1c3c4ad29eb747b327b17bb42e4c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293835,
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
      "evaluated_at": 1760293835
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
  "sig": "b3cfc8b4784ca9c16b2675ed152909acff4c2c303b0418c2397bc3d33f80a6db"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 2128275674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9417149}}}