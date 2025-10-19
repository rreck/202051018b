```json
{
  "id": "3e3f4e24bda6be46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292235,
  "host_pid": "9e6742732c60:1",
  "hash": "3b18e965c35278f7ea032e50e58cdc7ff671e0b4b3817cab48b72eafda89785d",
  "cid": "QmV13b18e965c35278f7ea032e50e58cdc7ff671e0b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292235,
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
      "evaluated_at": 1760292235
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
  "sig": "35b2a50fb328ee42597e45218b402a1693e826f4e361666b50091b370e233f24"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279312604
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 22902731, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': '998be1a53ec99162'}}}