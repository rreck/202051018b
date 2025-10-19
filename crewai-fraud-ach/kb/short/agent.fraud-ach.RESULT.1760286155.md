```json
{
  "id": "a481340f4bc7bd90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286155,
  "host_pid": "9e6742732c60:1",
  "hash": "cb562527b661d877c774ad61edba15ff4b2555b99de6d84bc53684d6d5b9e1dd",
  "cid": "QmV1cb562527b661d877c774ad61edba15ff4b2555b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286155,
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
      "evaluated_at": 1760286155
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
  "sig": "719e1a675452cb45eb45a781db47a3bcf75d1c506b904fd0c17719e7196b471e"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 111000027783297
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': '92df9dc264d0d07b'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}