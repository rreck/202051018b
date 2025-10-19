```json
{
  "id": "ab4885abf702e7e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286027,
  "host_pid": "9e6742732c60:1",
  "hash": "5eeafa827236ee10e224bfd29310ccf1669cde5fd92b00f4e50f987e869fdbb8",
  "cid": "QmV15eeafa827236ee10e224bfd29310ccf1669cde5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286027,
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
      "evaluated_at": 1760286027
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
  "sig": "3382902cdb18e8c12b7f8d976a51c1ed6cd677519798ad12fa3f8f909e7b26b3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461315278
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': 'd87579b8c6b654cb'}}}