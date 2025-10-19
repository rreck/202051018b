```json
{
  "id": "cf26adfbbf612aac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286341,
  "host_pid": "9e6742732c60:1",
  "hash": "d34a94f37bc16c37adbe2151b9e2ce0704fc7d52c3af5d4430759d5f0981a3b1",
  "cid": "QmV1d34a94f37bc16c37adbe2151b9e2ce0704fc7d52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286341,
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
      "evaluated_at": 1760286341
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
  "sig": "fb2611d056f6fc2925dc51a67915cd3ba1a67b753c0d9cf44d8f6118441dcddc"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 204734332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.53, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306106}}}