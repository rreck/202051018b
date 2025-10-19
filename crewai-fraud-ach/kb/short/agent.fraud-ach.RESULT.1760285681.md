```json
{
  "id": "9bea17ad0039d880",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285681,
  "host_pid": "9e6742732c60:1",
  "hash": "bd3be42636bfcde08ebb491c45ea2a053ba5fbdf7224af6a7e0baa789d025ccf",
  "cid": "QmV1bd3be42636bfcde08ebb491c45ea2a053ba5fbdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285681,
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
      "evaluated_at": 1760285681
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
  "sig": "3c82125587ce77f0980be21596ed88f9bdd79fa27406e48a4d468774af3e6667"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 29076186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}