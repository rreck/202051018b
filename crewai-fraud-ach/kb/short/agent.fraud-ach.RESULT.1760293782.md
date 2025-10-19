```json
{
  "id": "6e99ee0d66fd4d92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293782,
  "host_pid": "9e6742732c60:1",
  "hash": "f8ad49ad3099877e95c0bfcbd8c33d33925873c84fa3ea76f75f4dc31b3d8a0b",
  "cid": "QmV1f8ad49ad3099877e95c0bfcbd8c33d33925873c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293782,
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
      "evaluated_at": 1760293782
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
  "sig": "842ce26859194b86e7596d48f6518d377b5434e3f199a6e995b480c58aad6db5"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 225000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}