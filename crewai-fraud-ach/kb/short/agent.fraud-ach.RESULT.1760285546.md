```json
{
  "id": "4b2e987c61bfd62a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285546,
  "host_pid": "9e6742732c60:1",
  "hash": "eeb5106f2c24009ad863684da79d2906b6384eefcb6def1ca1d257f287439fa9",
  "cid": "QmV1eeb5106f2c24009ad863684da79d2906b6384eef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285546,
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
      "evaluated_at": 1760285546
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
  "sig": "ef4eec3099630c2527a75d8c862bca4b8275027de62a51f1bd00a55ba7641ed0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 23598064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}