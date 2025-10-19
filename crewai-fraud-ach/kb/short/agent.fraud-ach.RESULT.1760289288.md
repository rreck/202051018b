```json
{
  "id": "a954163943becf3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289288,
  "host_pid": "9e6742732c60:1",
  "hash": "cf919bcdf7a751d289e8e5764c0f221f8fe850a0539606bcb38f724c57fabde7",
  "cid": "QmV1cf919bcdf7a751d289e8e5764c0f221f8fe850a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289288,
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
      "evaluated_at": 1760289288
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
  "sig": "f8a6aa648c624d503a2a5f01b2652290a0bc8b854ee4f8c5044096ed015bea1f"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270720281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 1099228109, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9237211}}}