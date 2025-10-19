```json
{
  "id": "a65addaea9facd3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292776,
  "host_pid": "9e6742732c60:1",
  "hash": "852bf3c4b3b62f4be2025640f913153420c07e206399350e8cf8f67e4a72355b",
  "cid": "QmV1852bf3c4b3b62f4be2025640f913153420c07e20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292776,
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
      "evaluated_at": 1760292776
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
  "sig": "ea1d31d88fc6fee7a55f52842669880a37a72000c1d77b8e853e53ac2236ae3e"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 021000021072241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 1979472005, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'ac02650f27bf80d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.08, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9655961}}}