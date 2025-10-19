```json
{
  "id": "c12717464157d777",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287359,
  "host_pid": "9e6742732c60:1",
  "hash": "a65af5653b36a808e6261ea8b7c1bcba0be896ca1522252133187d0e4dce6f14",
  "cid": "QmV1a65af5653b36a808e6261ea8b7c1bcba0be896ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287359,
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
      "evaluated_at": 1760287359
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
  "sig": "4f9f3577fc497305cfb50c2d63a78fafa856c035b5fcd9eee4b445220a49d111"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243684464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 10275789, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': '4ae1f96c7cecc03b'}}}