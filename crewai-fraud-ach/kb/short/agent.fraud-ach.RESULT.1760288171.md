```json
{
  "id": "3808cebb61bb2939",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288171,
  "host_pid": "9e6742732c60:1",
  "hash": "f9ad2ff1f200669f24877740571f037f135c5561df6c5ed8fd45dc383c9d2d0e",
  "cid": "QmV1f9ad2ff1f200669f24877740571f037f135c5561",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288171,
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
      "evaluated_at": 1760288171
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
  "sig": "9f998764275de97c094d93bd174ad6e81ad325b7de42a9b21322a76c2d38c3d7"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000241606573
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 42500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '2fa99cb8a6f007e0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}