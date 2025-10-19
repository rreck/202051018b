```json
{
  "id": "286cba71b2025943",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285257,
  "host_pid": "9e6742732c60:1",
  "hash": "5127a64cfd9b8e0ac5dea202ba47b3b2f4b4ecb1d2b46e661cd950af530ddd44",
  "cid": "QmV15127a64cfd9b8e0ac5dea202ba47b3b2f4b4ecb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285257,
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
      "evaluated_at": 1760285257
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
  "sig": "c2599617e3d06b9ef5254af2538afb816c5a945b868b7b9a4369222c597e7d21"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100272560065
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}