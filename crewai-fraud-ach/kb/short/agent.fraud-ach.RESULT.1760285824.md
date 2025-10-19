```json
{
  "id": "54cc9aff6d589b16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285824,
  "host_pid": "9e6742732c60:1",
  "hash": "170b47197951830b4368b4106fb22448dae8a7c658de306c88857d84d80f2241",
  "cid": "QmV1170b47197951830b4368b4106fb22448dae8a7c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285824,
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
      "evaluated_at": 1760285824
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
  "sig": "8fe75453f5c6d62206d7ea859773da2515459f45bc1d8c104c0b8030fd010ebc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027931714
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285764, 'matching_hash': 'e2e3d7aa40c6ad9f'}}}