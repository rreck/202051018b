```json
{
  "id": "73e337d829bb947f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294780,
  "host_pid": "9e6742732c60:1",
  "hash": "701d06fd191ee477200fa824ab731dfc6c2b0accfc1f59fb49d8f819fb5188fc",
  "cid": "QmV1701d06fd191ee477200fa824ab731dfc6c2b0acc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294780,
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
      "evaluated_at": 1760294780
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
  "sig": "063d98c0ecb98f43279a76ed9bea4d61532b46e5f7f0ccec4afbd932a615a95e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 96619608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}