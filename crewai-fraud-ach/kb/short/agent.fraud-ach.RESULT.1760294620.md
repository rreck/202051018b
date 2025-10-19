```json
{
  "id": "896e5d79983c18c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294620,
  "host_pid": "9e6742732c60:1",
  "hash": "b19fe146836208269c675cdb3f663d1f6a7fc8ed48917e1ba5a02240b713122b",
  "cid": "QmV1b19fe146836208269c675cdb3f663d1f6a7fc8ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294620,
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
      "evaluated_at": 1760294620
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
  "sig": "fb99185bf6c09f8935309a3cd602a8e73e96a9fd6caa2891ab92b5895e1c96cd"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 120500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}