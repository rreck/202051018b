```json
{
  "id": "10e3f072bf2a3cc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291367,
  "host_pid": "9e6742732c60:1",
  "hash": "cf571693511f41472a2d09ee622200904ceb12cec387a9ea30ed3f47c37f7e93",
  "cid": "QmV1cf571693511f41472a2d09ee622200904ceb12ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291367,
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
      "evaluated_at": 1760291367
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
  "sig": "46a47b0dd32f399bbe74e34555e524e8fc6c2e56ec6e636f18ab83d0781076b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 26617953, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}