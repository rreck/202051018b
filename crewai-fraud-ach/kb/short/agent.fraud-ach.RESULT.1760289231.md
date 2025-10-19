```json
{
  "id": "40fa008697ea7936",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289231,
  "host_pid": "9e6742732c60:1",
  "hash": "f78fa5341c3d8110dfb7827859e3ed4d90bbf84e4abce88616d3662f22218435",
  "cid": "QmV1f78fa5341c3d8110dfb7827859e3ed4d90bbf84e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289231,
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
      "evaluated_at": 1760289231
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
  "sig": "9e18d92e1e5766ebef1f881e0055039ec309548c6cc6d4f8a5923bdc8194632e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}