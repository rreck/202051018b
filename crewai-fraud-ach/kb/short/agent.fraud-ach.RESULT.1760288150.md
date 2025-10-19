```json
{
  "id": "5d73015fac86bd04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288150,
  "host_pid": "9e6742732c60:1",
  "hash": "8341134df72354ff6ed43e08253863e80500f5dfbcfe501d143658a7fc5825fa",
  "cid": "QmV18341134df72354ff6ed43e08253863e80500f5df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288150,
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
      "evaluated_at": 1760288150
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
  "sig": "9a281b60fd8740ebd091868d3c08a5a03c57da5f66c93d48fbab8bdd8eac5818"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}