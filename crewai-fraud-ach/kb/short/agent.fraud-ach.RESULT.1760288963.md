```json
{
  "id": "981bd3c9a1c09d35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288963,
  "host_pid": "9e6742732c60:1",
  "hash": "0991550a29919f49c722ef95c0aeadf57be92d71adbc5953e1a5d06e56a1ab37",
  "cid": "QmV10991550a29919f49c722ef95c0aeadf57be92d71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288963,
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
      "evaluated_at": 1760288963
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
  "sig": "d1e95b3f0af6d692e97afed4ed6bd708b304df39ade85108143c2ab5176f9442"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 11413608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}