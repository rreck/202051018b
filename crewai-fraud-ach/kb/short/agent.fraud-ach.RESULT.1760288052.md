```json
{
  "id": "ac305758c3153312",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288052,
  "host_pid": "9e6742732c60:1",
  "hash": "88b7bbf754adbe167097ef66920c67381dc13ad177303abddcaf01c0d7de3eba",
  "cid": "QmV188b7bbf754adbe167097ef66920c67381dc13ad1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288052,
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
      "evaluated_at": 1760288052
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
  "sig": "983f3175d8f009d811c560bc160dcca5da79b5135ac08c6dd24448b45cf1c8d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 11195982, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}