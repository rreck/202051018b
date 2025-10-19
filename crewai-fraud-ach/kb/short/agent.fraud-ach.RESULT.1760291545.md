```json
{
  "id": "48a15d81c8f52d7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291545,
  "host_pid": "9e6742732c60:1",
  "hash": "1f46ab4f6e942adc9d0c6eb2a282a336c4e36e25965f47de6453cf317dfec53d",
  "cid": "QmV11f46ab4f6e942adc9d0c6eb2a282a336c4e36e25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291545,
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
      "evaluated_at": 1760291545
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
  "sig": "c6b20fa3dc3d037252cc0def68695e1936c589fe3e797ca263d4b7097426613c"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201465841026
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 88500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}