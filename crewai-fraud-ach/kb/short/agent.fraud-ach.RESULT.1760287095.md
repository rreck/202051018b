```json
{
  "id": "fb790db3b08ff11a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287095,
  "host_pid": "9e6742732c60:1",
  "hash": "f87adf0c1339c874eb9fc322f02121c9ac6d696d6aad045d25bec939a478e060",
  "cid": "QmV1f87adf0c1339c874eb9fc322f02121c9ac6d696d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287095,
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
      "evaluated_at": 1760287095
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
  "sig": "0095ef93bd5444a286a290f253c145c0ac716ca72c7cf63fd8287bf88fc0b29c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025657387
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15263616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': '1be88e7372567f08'}}}