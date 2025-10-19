```json
{
  "id": "3305a6f47b959b33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292704,
  "host_pid": "9e6742732c60:1",
  "hash": "65eacf98f96c60a6ce5539e391e2b304a0adf8bb37dafd46337539cda0041c37",
  "cid": "QmV165eacf98f96c60a6ce5539e391e2b304a0adf8bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292704,
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
      "evaluated_at": 1760292704
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
  "sig": "5080cd7eb52ebe34161061731e83da82c22e8f77b63d73ed7c332f8ff23429fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 29925042, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}