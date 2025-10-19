```json
{
  "id": "ec843eacc0229b74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290587,
  "host_pid": "9e6742732c60:1",
  "hash": "8b0239786605a7639fb5a9d85ac7e347f940fb7d8b25fca2c4353bb3b58fdccf",
  "cid": "QmV18b0239786605a7639fb5a9d85ac7e347f940fb7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290587,
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
      "evaluated_at": 1760290587
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
  "sig": "9f13a9e8b50c572e9c9717a8b4fc41c270efbac71b787dc0cc73b771f2290b07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270130572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 31474520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '3a095194dc4eaf85'}}}