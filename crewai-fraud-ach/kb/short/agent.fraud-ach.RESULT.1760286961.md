```json
{
  "id": "dc89eaad9e656f35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286961,
  "host_pid": "9e6742732c60:1",
  "hash": "f9c6598ed06d511e9aeca9ab4150190e3bd1e2aa4d4f9cfeb3ec35918b7c58c0",
  "cid": "QmV1f9c6598ed06d511e9aeca9ab4150190e3bd1e2aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286961,
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
      "evaluated_at": 1760286961
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
  "sig": "a1dc32176422e5b5a64f4e5376b090c15f1b8834ba6813d193c85a5b59ba541e"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}