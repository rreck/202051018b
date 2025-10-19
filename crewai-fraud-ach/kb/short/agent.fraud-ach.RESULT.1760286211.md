```json
{
  "id": "7da6c5d6e767d9e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286211,
  "host_pid": "9e6742732c60:1",
  "hash": "ad860e3d6cb5b787a8538b4f3f9f5c479fede7dc5bd3cb8a1aeb8764ec837c72",
  "cid": "QmV1ad860e3d6cb5b787a8538b4f3f9f5c479fede7dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286211,
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
      "evaluated_at": 1760286211
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
  "sig": "07ee056e7962a2b6b9f6edac95e60afa04646f838a3f43c0ac1b5c46bd7c8543"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461801118
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285764, 'matching_hash': '75b6b5cd12274a09'}}}