```json
{
  "id": "4eeb07be8c5f1824",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292716,
  "host_pid": "9e6742732c60:1",
  "hash": "1ae30d3a9d02818129c6416cc2ba175c3367829b5c8d37bd1e46a2964883d8e6",
  "cid": "QmV11ae30d3a9d02818129c6416cc2ba175c3367829b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292716,
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
      "evaluated_at": 1760292716
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
  "sig": "2ddcfb5f749c4da8f039a380eeee8fa8e89a66acead037eaebdcdaefb09a37e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022117413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 49966826, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': 'c7f16f3a9aa8490f'}}}