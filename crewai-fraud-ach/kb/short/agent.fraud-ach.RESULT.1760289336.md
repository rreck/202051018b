```json
{
  "id": "502cc798131914f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289336,
  "host_pid": "9e6742732c60:1",
  "hash": "3729f0fda7547f82520ad955dff6058210e8778207b751134eb84c4f53141660",
  "cid": "QmV13729f0fda7547f82520ad955dff6058210e87782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289336,
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
      "evaluated_at": 1760289336
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
  "sig": "7c1eea23fd3399b412bda80b7d8cddc2a96ea1a5ba20385da5d13925d8b2e169"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240953214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285764, 'matching_hash': 'cfdb33c4cfd6ba9b'}}}