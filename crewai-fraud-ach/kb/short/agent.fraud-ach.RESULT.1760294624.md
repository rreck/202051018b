```json
{
  "id": "f0df5e47c0625ab5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294624,
  "host_pid": "9e6742732c60:1",
  "hash": "a7aa8e26d7627f94a7084ccfe5b33237067beeea8da9861321a375b6a5a3349b",
  "cid": "QmV1a7aa8e26d7627f94a7084ccfe5b33237067beeea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294624,
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
      "evaluated_at": 1760294624
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
  "sig": "aafe8f81f256a6a7b65fe3d8b809687e3f13cac5ea0534c8f070d74492db6a50"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100273946283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 2337803630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': 'ff0c3c22534c93d5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.11, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9700430}}}