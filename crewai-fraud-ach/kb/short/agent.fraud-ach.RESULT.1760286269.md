```json
{
  "id": "8f3234675fe518ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286269,
  "host_pid": "9e6742732c60:1",
  "hash": "883064f77b066c9da03ad9794c83957f620c1e7598a280ba4d0f2c3f977d5b8f",
  "cid": "QmV1883064f77b066c9da03ad9794c83957f620c1e75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286269,
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
      "evaluated_at": 1760286269
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
  "sig": "5314d6fc28ad04858002b0bf824fac5a84c01824bb47dd37f8a36893b591c628"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000023724402
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': '3d4ab0f371876a2a'}}}