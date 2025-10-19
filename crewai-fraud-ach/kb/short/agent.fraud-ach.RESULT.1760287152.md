```json
{
  "id": "23c30cdcd65d267f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287152,
  "host_pid": "9e6742732c60:1",
  "hash": "9d1c31c38ecbeba9c5630b565ad522bf80a457a7207b3f966b8fc4da4ce8b62f",
  "cid": "QmV19d1c31c38ecbeba9c5630b565ad522bf80a457a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287152,
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
      "evaluated_at": 1760287152
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
  "sig": "030544c019eb2deece988723d41db52fa542b9365ac5d9faab408e2dbbada4a2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12959900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}