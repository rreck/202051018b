```json
{
  "id": "909725e8c6b5948d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285330,
  "host_pid": "9e6742732c60:1",
  "hash": "dffeee04c5423eb6c8a1c9bf97b2469e6a9df20a84eea16b4c1dba86be23e215",
  "cid": "QmV1dffeee04c5423eb6c8a1c9bf97b2469e6a9df20a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285330,
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
      "evaluated_at": 1760285330
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
  "sig": "a106167b0db6d0c1317ac095fc99905a2e5204fd82a80cfe51c471147fa5bf62"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 342842850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9795510}}}