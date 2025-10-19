```json
{
  "id": "22246fabef4e3575",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294887,
  "host_pid": "9e6742732c60:1",
  "hash": "0cf7d6c277a2d33cd4642e677b5cd85304aac70930448c4f68744e92b39c7265",
  "cid": "QmV10cf7d6c277a2d33cd4642e677b5cd85304aac709",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294887,
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
      "evaluated_at": 1760294887
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "bfa9418e0a7946fbd6be9e30273aa50856d86bca30fa08e0238d21bede4f168e"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028490637
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 123000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '1f028817acc0361c'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}