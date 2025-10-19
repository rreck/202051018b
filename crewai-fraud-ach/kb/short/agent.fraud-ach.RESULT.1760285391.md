```json
{
  "id": "9a6a26470d551c67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285391,
  "host_pid": "9e6742732c60:1",
  "hash": "cf799a56afdc50f0ab2bc7cabd2a3e1ba61712c794ae15423c581658185f8f4b",
  "cid": "QmV1cf799a56afdc50f0ab2bc7cabd2a3e1ba61712c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285391,
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
      "evaluated_at": 1760285391
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
  "sig": "55318dab73e21785fa1ace47fd9883907e2148a614a8ed21a067c292491eac8d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030656036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11667001, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760284979, 'matching_hash': '54d3add09935598e'}}}