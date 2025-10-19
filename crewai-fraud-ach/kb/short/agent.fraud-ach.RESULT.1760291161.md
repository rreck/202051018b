```json
{
  "id": "c0d7a979a737dcde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291161,
  "host_pid": "9e6742732c60:1",
  "hash": "54139ccedaa033d3310460c97a6bc87699c6aafd7a93e63146420434af9056c7",
  "cid": "QmV154139ccedaa033d3310460c97a6bc87699c6aafd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291161,
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
      "evaluated_at": 1760291161
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
  "sig": "2cecd4b0d3a97d95c5965d39b41572e584748ebeed2b21cbd78157f70a10b372"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 79088016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}