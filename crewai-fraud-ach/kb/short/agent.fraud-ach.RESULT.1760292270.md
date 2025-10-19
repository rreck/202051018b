```json
{
  "id": "235570351899205c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292270,
  "host_pid": "9e6742732c60:1",
  "hash": "162fe1f11b4a5d6494287149bb72520002415fba19a8ad8aca1418e8c6a2ce96",
  "cid": "QmV1162fe1f11b4a5d6494287149bb72520002415fba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292270,
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
      "evaluated_at": 1760292271
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
  "sig": "066c88fc6e9337a41918aab1abdc733951b8a04fedfdab17e8622d42afe0bbac"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 111000023893131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 1904619444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '5255bec7f5e0b39d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.18, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9817626}}}