```json
{
  "id": "220c33a53d7e98b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294775,
  "host_pid": "9e6742732c60:1",
  "hash": "c41afc5d12f0eb26e99a9ea5ce8ac80edb60dece0aa5b9c31beab50ebe7c3f79",
  "cid": "QmV1c41afc5d12f0eb26e99a9ea5ce8ac80edb60dece",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294775,
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
      "evaluated_at": 1760294775
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
  "sig": "3783dd52abdab8ef2395906af37646f0e8edd5d18601f25511d764da58dbea00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 100531416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}