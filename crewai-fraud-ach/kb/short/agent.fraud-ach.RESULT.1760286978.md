```json
{
  "id": "68a93c03429e4435",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286978,
  "host_pid": "9e6742732c60:1",
  "hash": "dcc296dd89c7a7fef618e4a27d22ba2a0302117969044f9dcde1d9589a5173a4",
  "cid": "QmV1dcc296dd89c7a7fef618e4a27d22ba2a03021179",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286978,
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
      "evaluated_at": 1760286978
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
  "sig": "3bec26e953467bee16ed3f5ee862551636e9c2561cac2c375f554eff1172eb64"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 021000028645436
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': '6242cc5f185f73d7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}