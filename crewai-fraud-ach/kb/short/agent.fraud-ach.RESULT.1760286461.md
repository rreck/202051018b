```json
{
  "id": "6a3c8f14b4582344",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286461,
  "host_pid": "9e6742732c60:1",
  "hash": "1a41081901ec8ac1175a72483b18c3840500d14d9473f1074968988d81716de0",
  "cid": "QmV11a41081901ec8ac1175a72483b18c3840500d14d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286461,
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
      "evaluated_at": 1760286461
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
  "sig": "8bc651be988cbbc62a462b0bda4adf9ef9329b393d91262563ba4c3e04102d63"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000020633236
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': 'c43a110d8b947858'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': 'cb8c3421a3879068'}}}