```json
{
  "id": "20bcfab19c604634",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292220,
  "host_pid": "9e6742732c60:1",
  "hash": "a3f0df0c003a728bbb5ea0bdfc033b215497dedce699e1c739f5f319cddbd6a4",
  "cid": "QmV1a3f0df0c003a728bbb5ea0bdfc033b215497dedc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292220,
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
      "evaluated_at": 1760292220
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "ea7f1ca08d1f691dbd8d8fa9a1c22e9ef9b8dbf988158c0384b25310c2b49172"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 031201463068676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 193000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': 'd6ede686f4e8ff6a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}