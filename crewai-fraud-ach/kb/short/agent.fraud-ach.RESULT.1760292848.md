```json
{
  "id": "11e8d7336463cf02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292848,
  "host_pid": "9e6742732c60:1",
  "hash": "00e701d0c53ed1649e5ae6b0fbec5b65c6b165c86f2bb8b778e07576c0392737",
  "cid": "QmV100e701d0c53ed1649e5ae6b0fbec5b65c6b165c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292848,
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
      "evaluated_at": 1760292848
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
  "sig": "8768aa8eb082897353c77b18afeb66c304e516f01950eacb60be6fa0e5b731d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022074928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 10300000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': 'a87d8bfbdd334181'}}}