```json
{
  "id": "9f87315d69975772",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294773,
  "host_pid": "9e6742732c60:1",
  "hash": "241630b01ae20add8934e076aae62eada8c81fd293cbe23ba9311507aaa304d0",
  "cid": "QmV1241630b01ae20add8934e076aae62eada8c81fd2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294773,
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
      "evaluated_at": 1760294773
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
  "sig": "27325abb9c6b316fc48f2b50095372e0d4a2454049e2dcb19578e9a9346784ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271976362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 98559408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}