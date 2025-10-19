```json
{
  "id": "1b09c88001d9b93a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286577,
  "host_pid": "9e6742732c60:1",
  "hash": "3633d77042814b8191447ced451df232e1c886bf52ec3042df06a0cd990d431c",
  "cid": "QmV13633d77042814b8191447ced451df232e1c886bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286577,
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
      "evaluated_at": 1760286577
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
  "sig": "975fd1a8396ce01a1c11106c1945c27b7450d32662add6ee26fd17de22ac9f53"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000024343993
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': '423e45fba5759e5c'}}}