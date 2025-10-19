```json
{
  "id": "88ba8b41772f5948",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286967,
  "host_pid": "9e6742732c60:1",
  "hash": "a537263fceb6165c8c9c9fe0df841bde5530ac8da82dee37ece92c384c5e86be",
  "cid": "QmV1a537263fceb6165c8c9c9fe0df841bde5530ac8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286967,
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
      "evaluated_at": 1760286967
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
  "sig": "54d7b017322fe48c17259c8a2eac0dc83fc642372ff1d07565c63b2bd58338e5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17837088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}