```json
{
  "id": "fcdeb1b1c623f792",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287349,
  "host_pid": "9e6742732c60:1",
  "hash": "92b85997343e73e70a7983d5b73a8e1495fd9b59fbf86eb90e14dc2edf3c49f3",
  "cid": "QmV192b85997343e73e70a7983d5b73a8e1495fd9b59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287349,
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
      "evaluated_at": 1760287349
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
  "sig": "2bc93e90dbc3cc58a9abdccd26307fbb3ba1169b39a195bf14eb9d199b22fd9f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000023390591
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 17841228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': '65b6a0d7e3017724'}}}