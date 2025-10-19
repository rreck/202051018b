```json
{
  "id": "d2d878733924e5b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287746,
  "host_pid": "9e6742732c60:1",
  "hash": "7724742f75015ce0cf84251a452b8d2f966a048c41206e2a01bfec7194878373",
  "cid": "QmV17724742f75015ce0cf84251a452b8d2f966a048c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287746,
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
      "evaluated_at": 1760287746
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
  "sig": "309f8813b7b2ace8226d2d6d5a7b54740fac24754013ecafed791718bbb6f342"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 22631250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}