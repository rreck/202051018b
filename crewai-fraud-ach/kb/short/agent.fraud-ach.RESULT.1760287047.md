```json
{
  "id": "d5d59f2c9a41090f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287047,
  "host_pid": "9e6742732c60:1",
  "hash": "e4e90e270bb9e6800f51dfaa5d28fe4c43cc794828c2d96657219551ae3dea9b",
  "cid": "QmV1e4e90e270bb9e6800f51dfaa5d28fe4c43cc7948",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287047,
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
      "evaluated_at": 1760287047
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
  "sig": "7a58d086bf0fa6962f2bb3a83c5699d14bae8987e7ee6f4cad52589ac9591534"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469526930
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}