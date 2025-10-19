```json
{
  "id": "35f05b86c4136688",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294288,
  "host_pid": "9e6742732c60:1",
  "hash": "91b64fd2569275354b57450b6b7a273b5b0877ccc1d9ae148c3bd54b21df7836",
  "cid": "QmV191b64fd2569275354b57450b6b7a273b5b0877cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294288,
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
      "evaluated_at": 1760294288
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
  "sig": "9fc9150763f1f9c8ceccf8e2ae3ba9f74afdda7ba0add943525b1056a2f29d50"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 114889620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}