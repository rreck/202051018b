```json
{
  "id": "64ef1ce366120e5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290076,
  "host_pid": "9e6742732c60:1",
  "hash": "5ee744425017127d1798fe989ad34a4828640c94420b2e70ee187eeee77de152",
  "cid": "QmV15ee744425017127d1798fe989ad34a4828640c94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290076,
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
      "evaluated_at": 1760290076
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
  "sig": "2e9ac3f27d873a0d9e8c5803c2661c3b5fc32299fe21564f945c3446c073ab8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 30921441, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}