```json
{
  "id": "50d4e8a777b15bca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293421,
  "host_pid": "9e6742732c60:1",
  "hash": "79c63114ed79a6145ce75950eb0d7cae3f71f515248d9a6f8753992b11c96706",
  "cid": "QmV179c63114ed79a6145ce75950eb0d7cae3f71f515",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293421,
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
      "evaluated_at": 1760293421
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
  "sig": "e681a899ac04cf1cc6029336c888cd104ed3380dc454341406c90d4874fe2a50"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 106578456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}