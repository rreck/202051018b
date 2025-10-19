```json
{
  "id": "5b0ad14de9170673",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294172,
  "host_pid": "9e6742732c60:1",
  "hash": "ebcf7f184c142cdf8258afbdf8fb11d8f1cd0a601314a4e3944cca2b8595c83e",
  "cid": "QmV1ebcf7f184c142cdf8258afbdf8fb11d8f1cd0a60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294172,
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
      "evaluated_at": 1760294172
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
  "sig": "4ff2a31f374de6d1c8a36c1a3ece1b6ca0ef05b1a9bbb750d658efadbc9b8105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033971595
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 104644028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': 'c20a798c67202fae'}}}