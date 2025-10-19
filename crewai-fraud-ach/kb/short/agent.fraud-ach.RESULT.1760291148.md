```json
{
  "id": "3f9650f66b11016c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291148,
  "host_pid": "9e6742732c60:1",
  "hash": "7c46e9f26c24b7fef149cca8255315c5e4d98f60b95d638be42389302b526d5b",
  "cid": "QmV17c46e9f26c24b7fef149cca8255315c5e4d98f60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291148,
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
      "evaluated_at": 1760291148
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
  "sig": "2f671dae69f1c3a49b741fea7c0edb01f1d686ef3da9f809068205ff188be3a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464866805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 64787352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': '8f846e2074b125b7'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}