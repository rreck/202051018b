```json
{
  "id": "4d7173c3e84cc386",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285927,
  "host_pid": "9e6742732c60:1",
  "hash": "2a497ae2f6181e2a86a416d0be9a61a6fb3bf20369ab7fa9143580b08005620a",
  "cid": "QmV12a497ae2f6181e2a86a416d0be9a61a6fb3bf203",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285927,
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
      "evaluated_at": 1760285927
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
  "sig": "5e7b26b5a63d8cca8c5741412262decc70677dd67037a6770e3f6b890f7a2324"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462408143
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}