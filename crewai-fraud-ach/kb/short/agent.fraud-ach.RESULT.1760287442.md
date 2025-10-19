```json
{
  "id": "a4c2336b83f164b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287442,
  "host_pid": "9e6742732c60:1",
  "hash": "54c982d369d9842069c55ac7e44d5c67aee5dac84e5bec87e5d71caa8e274deb",
  "cid": "QmV154c982d369d9842069c55ac7e44d5c67aee5dac8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287442,
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
      "evaluated_at": 1760287442
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
  "sig": "f95b2b5a09aa8a39ffcf6996c4f74885526f58c169aa81dec16b409fcea580a8"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 60000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}