```json
{
  "id": "30ef65068365ad7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291281,
  "host_pid": "9e6742732c60:1",
  "hash": "4283a8610860b9553ac123ac4e3e7713a6111ebf76d8e8b28056f88d3fa503cf",
  "cid": "QmV14283a8610860b9553ac123ac4e3e7713a6111ebf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291281,
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
      "evaluated_at": 1760291281
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
  "sig": "4476ac33d1ea1b4d28b5a6c37041b20d1d08ee777aa0d482305d65ef28aedecf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244838202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 59302230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}