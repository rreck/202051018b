```json
{
  "id": "5e73286a2987a570",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285247,
  "host_pid": "9e6742732c60:1",
  "hash": "3a7898c8c364a1f58160fd3b8f771bf8426ea049cc2e374b1c9f2b926b1e954c",
  "cid": "QmV13a7898c8c364a1f58160fd3b8f771bf8426ea049",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285247,
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
      "evaluated_at": 1760285247
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
  "sig": "41bd323e7bf5bd3fb14a1079db0cb006e0e3d82a4e77de2b35bcbff879bf0c34"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11377638, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}