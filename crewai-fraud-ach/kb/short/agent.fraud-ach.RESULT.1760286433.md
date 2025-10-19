```json
{
  "id": "4069d3ff5ccba50d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286433,
  "host_pid": "9e6742732c60:1",
  "hash": "97e671859a53ad0c8d0a4b5c59d5a4daccf47d53b3b37b725730d78fc2454e0d",
  "cid": "QmV197e671859a53ad0c8d0a4b5c59d5a4daccf47d53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286433,
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
      "evaluated_at": 1760286433
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
  "sig": "3666a0b6f81e65e134e4545ecdb122ccb26a6ca25e8c2bdff5a573e27a82b12e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243649474
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '901672e1b111b3e4'}}}