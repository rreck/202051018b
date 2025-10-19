```json
{
  "id": "2221a2a1856dcf81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286399,
  "host_pid": "9e6742732c60:1",
  "hash": "9d1abdd3d1832612dc7bc867e5f42f5014993716d7406fd6344a29c0c39a29d5",
  "cid": "QmV19d1abdd3d1832612dc7bc867e5f42f5014993716",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286399,
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
      "evaluated_at": 1760286399
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
  "sig": "2918068f7757e58e481d073c2a30b79e10ab2cc3067421e758e69e07d03e4c99"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246662267
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10230456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '95edcdc5f9712ce3'}}}60284979, 'matching_hash': '76eefa6b67e55304'}}}ore': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}}