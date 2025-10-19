```json
{
  "id": "bcabcd1f10e77a9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286907,
  "host_pid": "9e6742732c60:1",
  "hash": "e6d2e86ee7c7a03496f4236c4e2f791ae28dc9ed11fc1eb3b89064ea8adff3e5",
  "cid": "QmV1e6d2e86ee7c7a03496f4236c4e2f791ae28dc9ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286907,
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
      "evaluated_at": 1760286907
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
  "sig": "6f2a64137b8db1b4e6567bf38762fa216448d5c7146af47affa62138aaa95ba3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154242410
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': '26a9af32f02bfdfc'}}}