```json
{
  "id": "2a6d55bdfe3abb98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286936,
  "host_pid": "9e6742732c60:1",
  "hash": "d66bbee5b0087091da0e4d0bcfc57ccc7ffe024fe3366de48009a41a0baac254",
  "cid": "QmV1d66bbee5b0087091da0e4d0bcfc57ccc7ffe024f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286936,
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
      "evaluated_at": 1760286936
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
  "sig": "7a0e113a0b59b68948eeda621dedaaf5bf4ac8e5c82b19430ba10235ae6a72a7"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 026009595707011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 289195704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': 'bce5819bd1402454'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6885612}}}