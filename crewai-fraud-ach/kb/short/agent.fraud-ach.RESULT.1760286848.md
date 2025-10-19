```json
{
  "id": "df8f772df61dd9c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286848,
  "host_pid": "9e6742732c60:1",
  "hash": "1159325082afb737d621031245bf43ddc098bb4ae38657772440b2ba3de85f00",
  "cid": "QmV11159325082afb737d621031245bf43ddc098bb4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286848,
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
      "evaluated_at": 1760286848
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
  "sig": "2cf2717588a109369edb3bda8104a6cecc397ad63d02ad2c9e3dbbf6686b47ef"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 219913551, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5638809}}}