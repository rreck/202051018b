```json
{
  "id": "118d7fe361e77a71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286365,
  "host_pid": "9e6742732c60:1",
  "hash": "0663090c9d046dded30ffc856bfd48c596d7185f792065069deda2908ad6ccad",
  "cid": "QmV10663090c9d046dded30ffc856bfd48c596d7185f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286365,
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
      "evaluated_at": 1760286365
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
  "sig": "5bdf66c18875c8ed53f38a393391cdb5f110c491094114a2adc7f8c328ea654d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461197823
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}