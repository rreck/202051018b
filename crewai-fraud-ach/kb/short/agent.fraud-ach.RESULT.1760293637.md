```json
{
  "id": "1297b4e3a744daab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293637,
  "host_pid": "9e6742732c60:1",
  "hash": "065fb14b240b0d21384d9a1aa0e2853b74961508bd2548c1dc61806e416b3f36",
  "cid": "QmV1065fb14b240b0d21384d9a1aa0e2853b74961508",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293637,
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
      "evaluated_at": 1760293637
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
  "sig": "22ffc79c86fa2a0a24a085a44dd3e8212e1c4fe29b5d77ba73a1220c52d79505"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460708628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 11100000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}