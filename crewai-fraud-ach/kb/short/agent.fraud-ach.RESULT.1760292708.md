```json
{
  "id": "95e923fe5b5c89b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292708,
  "host_pid": "9e6742732c60:1",
  "hash": "d2dec4641c27b13efc6318e5e1a18e9b392d6c24cd3f83f23ed4f2568b85e848",
  "cid": "QmV1d2dec4641c27b13efc6318e5e1a18e9b392d6c24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292708,
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
      "evaluated_at": 1760292708
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
  "sig": "5a7032cb75b1006bc939e1b1f445c48e518059fab27dcb7465cd28de98e20371"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 1892627261, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.9, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9323287}}}