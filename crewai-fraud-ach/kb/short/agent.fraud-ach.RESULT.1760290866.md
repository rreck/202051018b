```json
{
  "id": "e328f5dc5ca9d365",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290866,
  "host_pid": "9e6742732c60:1",
  "hash": "90be2c394a0db81cce14ca6945f5182fffbc7463406da605d7009ba0123f3a5f",
  "cid": "QmV190be2c394a0db81cce14ca6945f5182fffbc7463",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290866,
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
      "evaluated_at": 1760290866
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
  "sig": "ac291bb0a6993c98eeefad7e995295804f2da551fced71a66701cde45285b0b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271276448
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 34678917, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '1d19524912ca559b'}}}