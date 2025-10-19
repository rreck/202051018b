```json
{
  "id": "987f4186ad8f666b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287644,
  "host_pid": "9e6742732c60:1",
  "hash": "d2383cae45d2c2605fdc26c29a90a78fb41e6faf6c88c5805697a01d4bfa5e87",
  "cid": "QmV1d2383cae45d2c2605fdc26c29a90a78fb41e6faf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287644,
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
      "evaluated_at": 1760287644
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
  "sig": "93fd521315f76c572a6778bea7a05ce389c1862f9a7bf87eb9f06da5acd0c5e3"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 111000022318038
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 16111624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': 'c47c52aff7a65053'}}}