```json
{
  "id": "55d0232216895160",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287322,
  "host_pid": "9e6742732c60:1",
  "hash": "6d4df5ddaf9ac1daa456c6262e8946fc43b95877b297dfa96bc0c91b84c22284",
  "cid": "QmV16d4df5ddaf9ac1daa456c6262e8946fc43b95877",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287322,
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
      "evaluated_at": 1760287322
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "59c342e7bc4cdbe3de7d5379648cc2fa7045f2ec73138bf2a9768700552a50d8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 11040232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}