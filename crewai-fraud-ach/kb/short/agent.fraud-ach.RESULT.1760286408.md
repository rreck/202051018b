```json
{
  "id": "03778c2f37b12cf7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286408,
  "host_pid": "9e6742732c60:1",
  "hash": "beb389764dc439832033da178e2b2d9abba2a98a02828c462c923dea9f49fa8f",
  "cid": "QmV1beb389764dc439832033da178e2b2d9abba2a98a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286408,
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
      "evaluated_at": 1760286408
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
  "sig": "37875f19f80e6b527f44855bcc21ca5e1e19acc7fc5ba93f37c1a0b6489292d7"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 031201467009203
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 190410528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': 'e7911512dd8ff7c4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7933772}}}