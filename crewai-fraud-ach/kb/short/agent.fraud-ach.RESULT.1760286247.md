```json
{
  "id": "4cfc9c05162ab49b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286247,
  "host_pid": "9e6742732c60:1",
  "hash": "b3d39b0ab6fb96ccb394b8f97c2ec3e70f944463e5c1d40e7bee6135c73fd73f",
  "cid": "QmV1b3d39b0ab6fb96ccb394b8f97c2ec3e70f944463",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286247,
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
      "evaluated_at": 1760286247
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
  "sig": "2df624b4dd9d36df8ad68398f3b79fa2ef538a7b9f440df9ca71bc1a4301f97e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000025895266
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}