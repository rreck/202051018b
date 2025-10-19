```json
{
  "id": "307289053741fc57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285912,
  "host_pid": "9e6742732c60:1",
  "hash": "ce20d81ee79b462c418b1e5c94f24737c22a2d37258657ef4e698ac586a36c49",
  "cid": "QmV1ce20d81ee79b462c418b1e5c94f24737c22a2d37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285912,
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
      "evaluated_at": 1760285912
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
  "sig": "3d940805bca6b85ca7126b32359730df5e72092f3ef55096631eb1e8f83ffc64"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 122105150872647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 57674928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': 'f142eb53d77ea00a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7209366}}}