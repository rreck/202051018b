```json
{
  "id": "813f76eae5208fd2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287554,
  "host_pid": "9e6742732c60:1",
  "hash": "dd7bd918afa567c54eb241adf22beb80eeddfeeb8c3ebf4884f2439e00b550a7",
  "cid": "QmV1dd7bd918afa567c54eb241adf22beb80eeddfeeb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287554,
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
      "evaluated_at": 1760287554
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
  "sig": "755aba0b3708e00ec3e4036e734a6b6eea97da6b0c850cbaf7e806b9333d1fda"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}