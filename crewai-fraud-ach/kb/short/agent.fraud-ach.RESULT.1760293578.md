```json
{
  "id": "b7c726fd1c3b9d40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293578,
  "host_pid": "9e6742732c60:1",
  "hash": "fa33ed5a0a845bb2dd3dc140c23e059b159e60f32568cb0ff306293a3acbcda3",
  "cid": "QmV1fa33ed5a0a845bb2dd3dc140c23e059b159e60f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293578,
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
      "evaluated_at": 1760293578
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
  "sig": "23664cd37f8a6c33e143f70ae6e4853d484209deff7a9df8cddedde24845ea69"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 122105150198952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 1841908146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '35a36fb353493cca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.33, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8334426}}}