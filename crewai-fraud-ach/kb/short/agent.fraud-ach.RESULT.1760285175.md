```json
{
  "id": "79eb36158ce8e346",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285175,
  "host_pid": "9e6742732c60:1",
  "hash": "6e8b23267c875c6441ab6c4b65b48ceae370160751d70571d8a85875867d1fe5",
  "cid": "QmV16e8b23267c875c6441ab6c4b65b48ceae3701607",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285175,
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
      "evaluated_at": 1760285175
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
  "sig": "7ef64c8ab6eb939d174073a1a1a21743a99677d9548fbed9a107d677c9fa3e88"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}