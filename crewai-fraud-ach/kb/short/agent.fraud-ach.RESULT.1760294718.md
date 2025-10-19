```json
{
  "id": "50891a83074bf47d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294718,
  "host_pid": "9e6742732c60:1",
  "hash": "361e0fe60c253f7dd4f57907c3f9f8fcca691fc4167e6c332397e3604bf5dc84",
  "cid": "QmV1361e0fe60c253f7dd4f57907c3f9f8fcca691fc4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294718,
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
      "evaluated_at": 1760294718
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
  "sig": "c3f65361e0c3c769888169c00b7d4d95588b322826535e866c5bfc1fec8f1cf4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 319, 'threshold': 50, 'total_amount': 60091625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 318, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}