```json
{
  "id": "e81072813dae186a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286615,
  "host_pid": "9e6742732c60:1",
  "hash": "9f102a53aaaa7525c859a01bc62487a666ffe16e10a3ef0df09de3941f661fbf",
  "cid": "QmV19f102a53aaaa7525c859a01bc62487a666ffe16e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286615,
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
      "evaluated_at": 1760286615
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
  "sig": "36c5836e738be87da7d61fb57622ab95dc4b8b4a4e767d2dd958a748ff8d8fc9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15471387, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}