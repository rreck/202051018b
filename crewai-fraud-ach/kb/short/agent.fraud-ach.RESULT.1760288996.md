```json
{
  "id": "5487fb6f17fee6bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288996,
  "host_pid": "9e6742732c60:1",
  "hash": "2e1c3de2cdbefa836a34fd3e8d54213393b84abf64dd9f10270be14bd0615fd2",
  "cid": "QmV12e1c3de2cdbefa836a34fd3e8d54213393b84abf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288996,
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
      "evaluated_at": 1760288996
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
  "sig": "4dfbca3bd8cf75a8b1096b32b1974546c7a71c8a6c97e9f3cd41124340ea22a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592552790
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 36084950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285764, 'matching_hash': 'c5daecdc9bc16873'}}}