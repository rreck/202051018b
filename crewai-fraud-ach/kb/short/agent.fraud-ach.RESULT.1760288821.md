```json
{
  "id": "3baeefe222445b5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288821,
  "host_pid": "9e6742732c60:1",
  "hash": "134108879e24e8a9d6e0dd534c9b8ec1a625789eab400b507dd86704eb827b94",
  "cid": "QmV1134108879e24e8a9d6e0dd534c9b8ec1a625789e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288821,
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
      "evaluated_at": 1760288821
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
  "sig": "9e6b39526a15e5dd0f59c07925e9ebaac666c3b9f6e0594bcb789aa5b16300fc"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463963144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 52500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': '4b7135c5b7384c49'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}