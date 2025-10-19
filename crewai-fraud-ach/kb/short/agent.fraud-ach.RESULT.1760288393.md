```json
{
  "id": "15abb4319ddb8149",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288393,
  "host_pid": "9e6742732c60:1",
  "hash": "cb23b783fa4eec6f70f2b2fea806c9c1dd1d442c2d77719d5e1adcdcc992ee93",
  "cid": "QmV1cb23b783fa4eec6f70f2b2fea806c9c1dd1d442c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288393,
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
      "evaluated_at": 1760288393
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
  "sig": "ef4f505f4abe90c287e52d8e71491b11f854d5efaab7a344569e4dfb0d783867"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 23846216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}