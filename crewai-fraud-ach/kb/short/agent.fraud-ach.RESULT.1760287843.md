```json
{
  "id": "44489bcba195eae0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287843,
  "host_pid": "9e6742732c60:1",
  "hash": "228a64260305435858562a39ef61d61bc2bfe7c6d4da27e63f57f5d0b303a55e",
  "cid": "QmV1228a64260305435858562a39ef61d61bc2bfe7c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287843,
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
      "evaluated_at": 1760287843
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
  "sig": "738a7626a17dc081b746fcd6db967e214b4fb14f458dc2772ed06fc2476a5f7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247969582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 74218950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}