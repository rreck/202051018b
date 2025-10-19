```json
{
  "id": "ec6e92e033f8570b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286428,
  "host_pid": "9e6742732c60:1",
  "hash": "ddd82aafa326939f5943748383dd165c08e56a3431f8a52caf32d77e7227ef71",
  "cid": "QmV1ddd82aafa326939f5943748383dd165c08e56a34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286428,
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
      "evaluated_at": 1760286428
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
  "sig": "659afb7c3a22c1bf95563b003dce863ba1bff2951d751e066550b93fa8463de7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105158395869
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '78e23c3ea29c8ae5'}}}