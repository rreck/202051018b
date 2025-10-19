```json
{
  "id": "b7d908f4eba61255",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293437,
  "host_pid": "9e6742732c60:1",
  "hash": "1ee7d8db1dad06d9b24a04e528ba4451e7112e5fc15a41dc4c807514749b093c",
  "cid": "QmV11ee7d8db1dad06d9b24a04e528ba4451e7112e5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293437,
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
      "evaluated_at": 1760293437
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
  "sig": "2eb9658f25a108e41c5ecc186833d7717e14e8e8764e9c7d3ce9e240db4efe6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242007664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 31555282, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': 'b61887453511199f'}}}