```json
{
  "id": "9926458671c75cf7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288792,
  "host_pid": "9e6742732c60:1",
  "hash": "27a0df81412a25458238ceadcb43305891e9754e6d0a224404e2dac641f5e065",
  "cid": "QmV127a0df81412a25458238ceadcb43305891e9754e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288792,
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
      "evaluated_at": 1760288792
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
  "sig": "595f2f8a755a7b37b22488a3429cfb41e4155c0a90b60998cf53487c1a94bfe9"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201460873764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 52000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '6dda2db9e90937c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}