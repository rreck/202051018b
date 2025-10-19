```json
{
  "id": "644bebc1b5e57009",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287640,
  "host_pid": "9e6742732c60:1",
  "hash": "d64c938f7f0f2e3166f22bea138e86e3e842fe6f136de49be46a62f4d290d998",
  "cid": "QmV1d64c938f7f0f2e3166f22bea138e86e3e842fe6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287640,
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
      "evaluated_at": 1760287640
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
  "sig": "27602e27ceb703dfe9f2c50dde39d7e6bda39877da6add1658477d3e044b51fe"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 121000240953214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285764, 'matching_hash': 'cfdb33c4cfd6ba9b'}}}