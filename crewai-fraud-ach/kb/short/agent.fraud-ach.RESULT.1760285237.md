```json
{
  "id": "fcdd2be623e2948e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285237,
  "host_pid": "9e6742732c60:1",
  "hash": "e89315b75e954834146c2b26808fa722af0ed46cc1c2b9162b19702e948aa757",
  "cid": "QmV1e89315b75e954834146c2b26808fa722af0ed46c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285237,
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
      "evaluated_at": 1760285237
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
  "sig": "0f8b9c96fa4db3c4bcaeb7144ecf55298e7fa7d73930722865f02b6345a10909"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10956244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}