```json
{
  "id": "44a24e961f076cbd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285753,
  "host_pid": "9e6742732c60:1",
  "hash": "cd5b8cf279d7f71915801bac8ef6a2b2022b13f40524bfdb62185c73cc0e9e86",
  "cid": "QmV1cd5b8cf279d7f71915801bac8ef6a2b2022b13f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285753,
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
      "evaluated_at": 1760285753
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
  "sig": "a8d74d15205f6f97a7c2326f28c99d0659c021ea8d2fd7bce3c49a5eefc15188"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 32025944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}