```json
{
  "id": "cc5f1aa377a333b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292520,
  "host_pid": "9e6742732c60:1",
  "hash": "cfb43833853e52c52047e6c3b9d8022874fcd7d199b6efce300546e2cf0986a6",
  "cid": "QmV1cfb43833853e52c52047e6c3b9d8022874fcd7d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292520,
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
      "evaluated_at": 1760292520
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
  "sig": "e1584be8ebbca3eb78e2faa46fef38e4952d339ee1867a600f7784fbb97f5363"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 99500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}