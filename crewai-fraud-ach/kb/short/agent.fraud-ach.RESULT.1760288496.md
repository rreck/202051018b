```json
{
  "id": "31e6dbde09d840ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288496,
  "host_pid": "9e6742732c60:1",
  "hash": "e91bd9791997dbb4a06966d5d5adfb1b550f216cd015ea793639541c0495c6f4",
  "cid": "QmV1e91bd9791997dbb4a06966d5d5adfb1b550f216c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288496,
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
      "evaluated_at": 1760288496
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
  "sig": "8af1671408e4174e54bca0f3c57a96f212d484f4f0d9a02861f44a832ed79cea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 32212125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}