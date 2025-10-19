```json
{
  "id": "b756170ba5d0644b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286278,
  "host_pid": "9e6742732c60:1",
  "hash": "8f1c010cb4789d746a143c4e5006e8e07b599060fb3c46fddaca5d51efbdbd0c",
  "cid": "QmV18f1c010cb4789d746a143c4e5006e8e07b599060",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286278,
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
      "evaluated_at": 1760286278
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
  "sig": "aecdff60a8fb121cce86aafc4b9bbe8c8aabe3dc403c4624c3d14f5115a008cf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245381675
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}