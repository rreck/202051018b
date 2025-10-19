```json
{
  "id": "edf6b6a4037dbc3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286979,
  "host_pid": "9e6742732c60:1",
  "hash": "4c79e97e8cb03438a908f93ab9be92a7e4b409fd2e31b38733fb6b7fb8e28f3d",
  "cid": "QmV14c79e97e8cb03438a908f93ab9be92a7e4b409fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286979,
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
      "evaluated_at": 1760286979
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
  "sig": "b959a071f5f52b7a846524e5a9a44812f97e6cd0845dfb8bc8e6e37ad2a76e9f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278631812
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'e154fa328ed40444'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': 'd8f9033e4ee0a57f'}}}