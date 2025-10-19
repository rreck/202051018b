```json
{
  "id": "9816609a0bad317b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286561,
  "host_pid": "9e6742732c60:1",
  "hash": "813c04f88be3e4c4eb31f1245f083858b27bf8eb12c7a93d39353f5f5430c4bf",
  "cid": "QmV1813c04f88be3e4c4eb31f1245f083858b27bf8eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286561,
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
      "evaluated_at": 1760286561
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
  "sig": "760761a3c59acd4c60aa3ce0e47607bfed799a3d820c288d5f0222f92903aedc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000032712851
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}