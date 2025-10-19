```json
{
  "id": "f9d2e1cc9c8dc1d4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292685,
  "host_pid": "9e6742732c60:1",
  "hash": "c6e5b8fbc2e94d1f8bb581d12ca6b326ab389c462f3c3998e368709d89dd5f30",
  "cid": "QmV1c6e5b8fbc2e94d1f8bb581d12ca6b326ab389c46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292685,
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
      "evaluated_at": 1760292685
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
  "sig": "d0ba4551a0d7d46f59f9896b105cccb89b38a992e2aa20791b73c3825df06b2a"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000241606573
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 101500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '2fa99cb8a6f007e0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}