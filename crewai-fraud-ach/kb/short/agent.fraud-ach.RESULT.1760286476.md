```json
{
  "id": "7885136a68b28537",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286476,
  "host_pid": "9e6742732c60:1",
  "hash": "282f7f05c6545e226244be48ae94416810a9bd7ae0c7ddfe01e703f7403f9099",
  "cid": "QmV1282f7f05c6545e226244be48ae94416810a9bd7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286476,
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
      "evaluated_at": 1760286476
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
  "sig": "f702c913ff44ab4c9c9502d38315eaf3022004cb0ba5ee31494d5a08f9f63002"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}