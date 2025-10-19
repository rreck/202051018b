```json
{
  "id": "affd7a30e68268dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287376,
  "host_pid": "9e6742732c60:1",
  "hash": "96d93d7bc568d789fde7102f0a7e091dd64538d5d2c65a1acf7e390e418fa887",
  "cid": "QmV196d93d7bc568d789fde7102f0a7e091dd64538d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287376,
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
      "evaluated_at": 1760287376
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "da1257879a427714bf8dc38a5c4b85591a64b747309ce85321c950c63ab76593"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009599855850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 20972452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}