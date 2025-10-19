```json
{
  "id": "08a66ed2dc6623f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291974,
  "host_pid": "9e6742732c60:1",
  "hash": "c2b1d2cac373a3a83ed3ed4966b844da8d77af5a13ba68a5e1b5a7752a078395",
  "cid": "QmV1c2b1d2cac373a3a83ed3ed4966b844da8d77af5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291974,
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
      "evaluated_at": 1760291974
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
  "sig": "6ab3247bf5ab222a007ad913e70837c7b14d787f210f5e95233f0fd132c1a7f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029285635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 65118823, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '952b5fd24342145c'}}}