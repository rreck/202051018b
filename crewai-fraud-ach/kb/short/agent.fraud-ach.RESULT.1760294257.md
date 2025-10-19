```json
{
  "id": "7741247b6881cbff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294257,
  "host_pid": "9e6742732c60:1",
  "hash": "6c7042014ad601b28fa3f2a8680eb7b050a5795b252943a15202814dcc9e31c6",
  "cid": "QmV16c7042014ad601b28fa3f2a8680eb7b050a5795b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294257,
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
      "evaluated_at": 1760294257
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
  "sig": "4d3c36e81c96fa764be305a271f47b422dcb4b8be566c52850010b3160702e5d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 74470032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}