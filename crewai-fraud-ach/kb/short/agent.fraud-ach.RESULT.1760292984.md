```json
{
  "id": "8a2943b6f84d69a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292984,
  "host_pid": "9e6742732c60:1",
  "hash": "91849a3da718469004c74126b52a7f3ac8f3674680141a83bce22ed07d57a56e",
  "cid": "QmV191849a3da718469004c74126b52a7f3ac8f36746",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292984,
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
      "evaluated_at": 1760292984
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
  "sig": "84d39aaeba97851e63a8928b4637ba5c7f0aa9abeaf98cc1379dc3e883484177"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 52250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}