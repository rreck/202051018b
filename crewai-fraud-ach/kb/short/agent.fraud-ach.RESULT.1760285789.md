```json
{
  "id": "f99dea188d329531",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285789,
  "host_pid": "9e6742732c60:488",
  "hash": "a7f8c97fc72b0e4b2de3a451a96f7c1d77b6c077717a0fb8d43cc921a5b8d3dc",
  "cid": "QmV1a7f8c97fc72b0e4b2de3a451a96f7c1d77b6c077",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:488",
      "created_at": 1760285789,
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
      "evaluated_at": 1760285789
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_medium"
  ],
  "sig": "1a38da955930d575fa71243d7d478fdc6e6d4f06c008df299af04f4a8f29c869"
}
```

Fraud detected: round_amount_pattern (score: 40)
Transaction: 031201462455734
Details: {'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}332294, 'iqr_bounds': {'lower': -401016.875, 'upper': 959042.125}, 'amount': 5595688}}}}