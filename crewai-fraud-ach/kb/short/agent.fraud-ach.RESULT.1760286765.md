```json
{
  "id": "d50c070d453bc06c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286765,
  "host_pid": "9e6742732c60:1",
  "hash": "2e6529d29881e2645140d0c473422168d404dfa070f451dc8e4fe8b81264e8b6",
  "cid": "QmV12e6529d29881e2645140d0c473422168d404dfa0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286765,
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
      "evaluated_at": 1760286765
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
  "sig": "09f7d05066b52ad13859c314321f760a21101a3fb6e71d20e35a1aa820c5e125"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 111000026237439
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 196636572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': '88704d1e07f02084'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5462127}}}