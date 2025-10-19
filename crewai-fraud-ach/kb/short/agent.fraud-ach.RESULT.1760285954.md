```json
{
  "id": "aac9e4dff3baab5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285954,
  "host_pid": "9e6742732c60:1",
  "hash": "a91c6e9594c59ec91b5aa6ba73c108a687c31898bd8cfb54263802c726f0edde",
  "cid": "QmV1a91c6e9594c59ec91b5aa6ba73c108a687c31898",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285954,
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
      "evaluated_at": 1760285954
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
  "sig": "f87ad36db5ed4704cb019e19cbd76c6ee0e8c087f76b86bb4fe2d6872ae9fe57"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022307864
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '183a325d3d521c29'}}}