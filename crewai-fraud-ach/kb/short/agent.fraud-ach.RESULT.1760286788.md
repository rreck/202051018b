```json
{
  "id": "63e0022da5f1d47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286788,
  "host_pid": "9e6742732c60:1",
  "hash": "a2dac951eebe93a3474242f53dcfceceb979b247f5a567416c830efe486cd873",
  "cid": "QmV1a2dac951eebe93a3474242f53dcfceceb979b247",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286788,
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
      "evaluated_at": 1760286788
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
  "sig": "7ca815d0cec72c7877c7c49b17cdcc521ad022660fe6f871ab5d3287587db21b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243340063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15683634, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '5f2724e98c8a67b0'}}}