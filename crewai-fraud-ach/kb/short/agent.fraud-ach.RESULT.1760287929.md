```json
{
  "id": "f1cb4f341ab7c5b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287929,
  "host_pid": "9e6742732c60:1",
  "hash": "05355c55dfeeea3c7710ca114255c607515f7ef076d1eb517963dbcce00877f2",
  "cid": "QmV105355c55dfeeea3c7710ca114255c607515f7ef0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287929,
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
      "evaluated_at": 1760287929
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
  "sig": "16153c84e73342146af89fd722e7ee903fea7eb02240750f1033ec186fc7e111"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 111000022658248
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 722305430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285764, 'matching_hash': '6b9326523c35dc7b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.57, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9380590}}}