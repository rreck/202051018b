```json
{
  "id": "a8a4d6343fd38415",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287073,
  "host_pid": "9e6742732c60:1",
  "hash": "bd3c8bf35614d0042298749dd2635ff140b3266bda7dd45e47d2906a934481b0",
  "cid": "QmV1bd3c8bf35614d0042298749dd2635ff140b3266b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287073,
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
      "evaluated_at": 1760287073
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
  "sig": "7666fc9a5615489f99d12c5de2ec0f11a1d8b6e7a14d309deb84ddd452f6abf9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13948895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}