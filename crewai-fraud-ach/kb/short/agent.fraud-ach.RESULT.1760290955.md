```json
{
  "id": "071b8ce94c0ba0d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290955,
  "host_pid": "9e6742732c60:1",
  "hash": "b4aca35b0972076164e03785aa14335a74153762c8e9dddfc97f346d3807cf8e",
  "cid": "QmV1b4aca35b0972076164e03785aa14335a74153762",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290955,
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
      "evaluated_at": 1760290955
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
  "sig": "f90bccf3e7e4fea799ff99205b25ac6eb83af7d5a91d8aba07bc6c3b95661a63"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 78573172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}