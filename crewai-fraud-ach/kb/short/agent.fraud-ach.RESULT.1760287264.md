```json
{
  "id": "3901c0ec12857b58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287264,
  "host_pid": "9e6742732c60:1",
  "hash": "82ed288bf473e61e88e14bb6a0d97108957ca1095522ca805695804853ab3812",
  "cid": "QmV182ed288bf473e61e88e14bb6a0d97108957ca109",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287264,
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
      "evaluated_at": 1760287264
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
  "sig": "fc75e81985bdccbbb0f4047bbdde18a7f70290c960d825d8c61c54aca39bf91d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 13996692, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}