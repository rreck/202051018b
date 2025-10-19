```json
{
  "id": "992a5b38dcb0972a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286881,
  "host_pid": "9e6742732c60:1",
  "hash": "9d06bb36c7141f12242fa7b2045a3345b75cd081a66c6aed5b435f22fda8dfdb",
  "cid": "QmV19d06bb36c7141f12242fa7b2045a3345b75cd081",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286881,
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
      "evaluated_at": 1760286881
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
  "sig": "fb1e3b7bb29c0c729c5d9c8ec4f19a4b8c08592a22e8211d8e51d6ddbaf38eca"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241355402
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}