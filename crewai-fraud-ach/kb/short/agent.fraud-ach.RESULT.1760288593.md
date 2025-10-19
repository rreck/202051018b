```json
{
  "id": "b337bca54b2fe9dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288593,
  "host_pid": "9e6742732c60:1",
  "hash": "e3c5633f84feb506d32e1bb562394552a739f9d820f4eea5dfd04efe4cf6b3df",
  "cid": "QmV1e3c5633f84feb506d32e1bb562394552a739f9d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288593,
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
      "evaluated_at": 1760288593
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
  "sig": "e8637eb618abaa846d59d8ece7234c5db59e87c012671553185c038ec50af6ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 48416900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}