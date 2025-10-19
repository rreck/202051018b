```json
{
  "id": "e0d2fe8a4a845031",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294576,
  "host_pid": "9e6742732c60:1",
  "hash": "a4ac3ce24a6d91cfe3849d9c4fc8d344cc76a6945aa209ab4269fb7524ceabac",
  "cid": "QmV1a4ac3ce24a6d91cfe3849d9c4fc8d344cc76a694",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294576,
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
      "evaluated_at": 1760294576
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
  "sig": "f32b1a13b1df684d1c081c54dfe7f8902de9894cd68c5e1d1ab429a9383f0107"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 76379520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}