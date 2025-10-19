```json
{
  "id": "01cdc402de869d42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287633,
  "host_pid": "9e6742732c60:1",
  "hash": "9fe30daee45418c16eeb63d5a1eca22e8aee9ef34e179c0e304380fd49fb1a37",
  "cid": "QmV19fe30daee45418c16eeb63d5a1eca22e8aee9ef3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287633,
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
      "evaluated_at": 1760287633
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
  "sig": "78974c9213501945a31107600016382f3957c9f640e3ab92f920cbc7a36cb7de"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 031201464396323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': 'e47699aa17e8c37e'}}}