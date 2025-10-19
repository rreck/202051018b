```json
{
  "id": "c3c35d4ab0b536d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292464,
  "host_pid": "9e6742732c60:1",
  "hash": "e19a491773ddc36c9282603e2f273725878d66bb22722584b02f171def11f3f9",
  "cid": "QmV1e19a491773ddc36c9282603e2f273725878d66bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292464,
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
      "evaluated_at": 1760292464
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "dd737b23bb196a1aa7ac40fa0bc64a4b9beca1e42557fbabdcb5ea944b9a77ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 96800616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}