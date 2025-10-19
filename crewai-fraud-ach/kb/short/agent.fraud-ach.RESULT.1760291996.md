```json
{
  "id": "e957158be1c714e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291996,
  "host_pid": "9e6742732c60:1",
  "hash": "6e54b8bf2d4364e9c6ca1fa0f219a0e89f345ca299cc180e18153ce590aa86d0",
  "cid": "QmV16e54b8bf2d4364e9c6ca1fa0f219a0e89f345ca2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291996,
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
      "evaluated_at": 1760291996
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
  "sig": "d5df17b33fba614a5eca5ab99f54931fd4913d04124418fe69d166554c4775f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 59925000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}