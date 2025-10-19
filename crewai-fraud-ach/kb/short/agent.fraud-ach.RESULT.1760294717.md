```json
{
  "id": "a34c90083ea84231",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294717,
  "host_pid": "9e6742732c60:1",
  "hash": "7f89c40f9ca7cb437c6bf5efd543a80584422bd56c07bcd3435577d3a79eee00",
  "cid": "QmV17f89c40f9ca7cb437c6bf5efd543a80584422bd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294717,
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
      "evaluated_at": 1760294717
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
  "sig": "1a83c7f5dddf4a55559ac4c95795e157ff7d73b1759813511cea2aed19d37006"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271259155
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 96130557, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '525a45536127a4d2'}}}