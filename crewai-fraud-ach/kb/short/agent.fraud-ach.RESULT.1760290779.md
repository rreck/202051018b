```json
{
  "id": "48c64ca26e4b25ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290779,
  "host_pid": "9e6742732c60:1",
  "hash": "2395e45a428a5c7590884cd91d227f6cedcb8c467a2b133329d184e74ebcc134",
  "cid": "QmV12395e45a428a5c7590884cd91d227f6cedcb8c46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290779,
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
      "evaluated_at": 1760290779
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
  "sig": "a1eee274b6a1b8dcf36bf2b2a76327ec4e53b9d22a90b6c1dee03cc5ce6090d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028289114
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 18898104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '2ad1c8bf27fe5526'}}}