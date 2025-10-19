```json
{
  "id": "7c5f0cd994131e96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289608,
  "host_pid": "9e6742732c60:1",
  "hash": "0139b76d92f1a903c955db23de196d47431b3580b45c6fc2b4bab5003e0720b2",
  "cid": "QmV10139b76d92f1a903c955db23de196d47431b3580",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289608,
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
      "evaluated_at": 1760289608
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
  "sig": "1c83abc820962b1a58ab9ebeedd76dfeec16d2f4c4bd8bbb6e09372fb8c1d455"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}een': 1760285764, 'matching_hash': 'a5f4ca8ac1007b12'}}}