```json
{
  "id": "d9b6a15eec241283",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287521,
  "host_pid": "9e6742732c60:1",
  "hash": "5925930db3d0a7c401e1c3dda0f0fc4fe8b785a7b6fff41ab7b3ed04a6609daf",
  "cid": "QmV15925930db3d0a7c401e1c3dda0f0fc4fe8b785a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287521,
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
      "evaluated_at": 1760287521
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
  "sig": "90ad1e1de975dcb04991e1792d7eeb52180dc549129971ae3df61d4a6d53d576"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 121000243890645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 11471985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}