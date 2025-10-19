```json
{
  "id": "680f72d88c3888a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292839,
  "host_pid": "9e6742732c60:1",
  "hash": "53a17c05e8d25b41785ef973750ecca1bc4e0d5dc4e2d1c1dca88b680cd7eccc",
  "cid": "QmV153a17c05e8d25b41785ef973750ecca1bc4e0d5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292839,
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
      "evaluated_at": 1760292839
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
  "sig": "8a6bdf74021933a50425f6f1024df4998c3eec860c66b293efa0471174d16576"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026302865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 61916184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '15ebb46c9afca80b'}}}