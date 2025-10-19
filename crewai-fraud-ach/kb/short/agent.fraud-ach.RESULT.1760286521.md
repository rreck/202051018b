```json
{
  "id": "e9900d8c3afe2d6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286521,
  "host_pid": "9e6742732c60:1",
  "hash": "dfc2b01c17648c30b428f1e44898c495ae4b132e16ee90fa6e2e4ad23ad7c58a",
  "cid": "QmV1dfc2b01c17648c30b428f1e44898c495ae4b132e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286521,
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
      "evaluated_at": 1760286521
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "f460f7d24b963c4d4663541758dc9ae53b9ef6172e4fbdd0cd7146ad5451d7f3"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 063100270473682
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 267332940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': 'dcfb2900505c6ddc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.64, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9547605}}}