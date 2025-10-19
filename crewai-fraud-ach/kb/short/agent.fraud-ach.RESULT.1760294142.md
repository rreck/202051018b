```json
{
  "id": "b45886bced55965d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294142,
  "host_pid": "9e6742732c60:1",
  "hash": "be603203b49f0a4f2a4924f5121246cba5abb49a3e26d6c4b60dcb23df30080e",
  "cid": "QmV1be603203b49f0a4f2a4924f5121246cba5abb49a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294142,
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
      "evaluated_at": 1760294142
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
  "sig": "acfd345ce5efd65aeaeb39f3d2208b15991981d5a64dfd7449693e9c0a6a2349"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 29513416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}