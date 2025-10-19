```json
{
  "id": "a01d5800340daff5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289095,
  "host_pid": "9e6742732c60:1",
  "hash": "ccef61f20e0fd29e9ef010dfa8a87b4bf4cc0c1c5f5e576df9f098cac5620a94",
  "cid": "QmV1ccef61f20e0fd29e9ef010dfa8a87b4bf4cc0c1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289095,
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
      "evaluated_at": 1760289095
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
  "sig": "64825f32c77ba4bd59561cc4c623e607aea6c5a77e44d71508d2c36af0d07cea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 33536705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}