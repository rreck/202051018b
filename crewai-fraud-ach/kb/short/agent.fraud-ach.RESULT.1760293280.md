```json
{
  "id": "6f87b6f74cfc9d59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293280,
  "host_pid": "9e6742732c60:1",
  "hash": "d019e5652ced6061ce9e7d62fdec7dd1314f9113e3921c8c1f3445bbef88cc80",
  "cid": "QmV1d019e5652ced6061ce9e7d62fdec7dd1314f9113",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293280,
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
      "evaluated_at": 1760293280
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
  "sig": "ead019d2433bc56e2930448785e5cd9931802f379c5b8aa52f98375f8b9a94c9"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000028604532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 2142812980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '4ce4a7b2afa8a7cc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.26, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9966572}}}