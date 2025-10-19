```json
{
  "id": "dd2269c71a804fcf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287409,
  "host_pid": "9e6742732c60:1",
  "hash": "72d1c8b9273cf3ad8b7e4af866fa0fb7c89cd4cfc3b1da807924aef05c1ca808",
  "cid": "QmV172d1c8b9273cf3ad8b7e4af866fa0fb7c89cd4cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287409,
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
      "evaluated_at": 1760287409
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "b10c4b451b210fd9e4d311597e65f0dbaa51463f10da937185b2dd4f250c75d4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009599908299
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 26035874, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': '494601c315920761'}}}553'}}}