```json
{
  "id": "a1bcbec7973511ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294374,
  "host_pid": "9e6742732c60:1",
  "hash": "6a5b982decdfe77cc13d2f3a74cb1fc1c2180a4a2d681dd5721f8e9a07cc9697",
  "cid": "QmV16a5b982decdfe77cc13d2f3a74cb1fc1c2180a4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294374,
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
      "evaluated_at": 1760294374
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
  "sig": "63d7fe061f0dd24b929796e0b9f633e1120d52dd92325da77e77e0a1acd364b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 14298210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}