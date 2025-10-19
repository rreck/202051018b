```json
{
  "id": "f4360ba0fe5e979a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294496,
  "host_pid": "9e6742732c60:1",
  "hash": "a376601f5cfc7a36a6426e4b474b9da813eeab5e400aa15d33c631b82fcf99ea",
  "cid": "QmV1a376601f5cfc7a36a6426e4b474b9da813eeab5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294496,
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
      "evaluated_at": 1760294496
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
  "sig": "05ff6feca56949f5beaddd64e1870a13930757f0daa1a05a8b5c9fed5f659395"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 97276585, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}