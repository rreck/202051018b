```json
{
  "id": "10b1c31a5cc3543d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287080,
  "host_pid": "9e6742732c60:1",
  "hash": "e126c553a8d974a48f002eda0b2f1d255322c27b6313460ac5ce4c6a527e5e52",
  "cid": "QmV1e126c553a8d974a48f002eda0b2f1d255322c27b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287080,
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
      "evaluated_at": 1760287080
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
  "sig": "7c8c7dfe64addaf720032177ea6c38fe48ff1c4a3846a43c7272f89e454f8a70"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000026914318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 459833430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285765, 'matching_hash': '634436741ef501a5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9783690}}}