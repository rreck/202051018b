```json
{
  "id": "0d0d00bfad3e1eb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292420,
  "host_pid": "9e6742732c60:1",
  "hash": "ea5ee727076b468ec2f5032b055db957f3109923885663bd3311ff2c54d6d383",
  "cid": "QmV1ea5ee727076b468ec2f5032b055db957f3109923",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292420,
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
      "evaluated_at": 1760292420
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
  "sig": "e967cb8f220d1997054d272764b17081460906b1b2e28f9500bd59f80d193174"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277826130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 12336928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': '6123129413abd06e'}}}