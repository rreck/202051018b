```json
{
  "id": "298caaa539212df5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290671,
  "host_pid": "9e6742732c60:1",
  "hash": "4819e04598c206ccd7b4982257f8e07220f5c5bb75d532ec427617d547fad356",
  "cid": "QmV14819e04598c206ccd7b4982257f8e07220f5c5bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290671,
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
      "evaluated_at": 1760290671
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
  "sig": "77ff5104d63aabab01255b96c4093466e235ff290108ca8939c0b8cc20052a69"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 59430228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}