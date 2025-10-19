```json
{
  "id": "60e04131616f72a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287749,
  "host_pid": "9e6742732c60:1",
  "hash": "cc04e0c1c90c126564dcbe60e7217dfd234ba77c2ef44bc6becb76705bd00e7a",
  "cid": "QmV1cc04e0c1c90c126564dcbe60e7217dfd234ba77c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287749,
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
      "evaluated_at": 1760287749
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
  "sig": "b670203ca5bd5d8f46cac9e39b4983aa61e31da986846e861d7ea3a18ba81054"
}
```

Fraud detected: round_amount_pattern (score: 72)
Transaction: 121000240623413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 35500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285764, 'matching_hash': 'b41427cac750dd0e'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}