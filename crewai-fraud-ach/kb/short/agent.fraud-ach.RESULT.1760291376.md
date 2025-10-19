```json
{
  "id": "2f29550be27cd4ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291376,
  "host_pid": "9e6742732c60:1",
  "hash": "c231c2b5773b3a8b020ecae4a632e3ca4d5f8dabb49fd96376c35d4a7f3cc4f4",
  "cid": "QmV1c231c2b5773b3a8b020ecae4a632e3ca4d5f8dab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291376,
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
      "evaluated_at": 1760291376
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
  "sig": "82f6c6464ce5d7a1b2150f32da87698c301ac15b45e10ca77cfdf2fbd391c53e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 51499159, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}