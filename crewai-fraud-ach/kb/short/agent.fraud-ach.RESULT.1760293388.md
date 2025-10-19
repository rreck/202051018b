```json
{
  "id": "021b458a013dda08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293388,
  "host_pid": "9e6742732c60:1",
  "hash": "0a0166653bedd1c29ba9bec018eea49f250a217b559f28e4f8f8fcaaabc83a15",
  "cid": "QmV10a0166653bedd1c29ba9bec018eea49f250a217b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293388,
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
      "evaluated_at": 1760293388
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
  "sig": "642cc63e2ea7b4556a4f3a806d16870b308e9081d61387f8a212379bbb381bec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025341515
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 54519948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}