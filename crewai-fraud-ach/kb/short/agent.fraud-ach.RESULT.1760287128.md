```json
{
  "id": "7b52ebfa1abbda42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287128,
  "host_pid": "9e6742732c60:1",
  "hash": "584ef4f631c9081d60b9b37ac90e8676d2e507f3d162f3d5cbed0b3c16987f8f",
  "cid": "QmV1584ef4f631c9081d60b9b37ac90e8676d2e507f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287128,
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
      "evaluated_at": 1760287128
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
  "sig": "20051c032dbdab2ca268ea2b1a0ca2ee63be971b2b484932d31a0294a305119e"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 418914916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.2, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8549284}}}