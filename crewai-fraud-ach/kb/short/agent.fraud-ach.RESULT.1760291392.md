```json
{
  "id": "22e3356fd2ea670d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291392,
  "host_pid": "9e6742732c60:1",
  "hash": "f051a2daf801e8bb7eca5399feeba840d2cdc9d0354835d6e8b3fd74cee418c6",
  "cid": "QmV1f051a2daf801e8bb7eca5399feeba840d2cdc9d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291392,
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
      "evaluated_at": 1760291392
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
  "sig": "ec375d7b68fa63c30e9db6f6255a7d7682e6a46f9c4894dcaf8b2ca131a71124"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279336195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 70289388, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'bc4c468b17fbec63'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}