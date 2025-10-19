```json
{
  "id": "fa2bd3ec274de49a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294463,
  "host_pid": "9e6742732c60:1",
  "hash": "9c663025a24e9fe6798d2eeaecb32f37c0b77d78195e416ee5b4bc9f2206a8f2",
  "cid": "QmV19c663025a24e9fe6798d2eeaecb32f37c0b77d78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294463,
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
      "evaluated_at": 1760294463
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
  "sig": "e012dac7d88e42d73aebdc851ce4dfbc0784a3f75e484d7a51926b9727ce3ec0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 38402966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}