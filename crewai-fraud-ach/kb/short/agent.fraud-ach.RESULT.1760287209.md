```json
{
  "id": "688e772be71c5a30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287209,
  "host_pid": "9e6742732c60:1",
  "hash": "f386ba7785a41cb32fa449e5d521b896e88a56e31d1e29deeb0c60dd34bf7108",
  "cid": "QmV1f386ba7785a41cb32fa449e5d521b896e88a56e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287209,
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
      "evaluated_at": 1760287209
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
  "sig": "6c47bc35ef31cce6aea1e76112895dff6e40a071353438d55d04a4ab9513569b"
}
```

Fraud detected: duplicate_transaction (score: 69)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 54, 'details': {'transaction_count': 52, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}