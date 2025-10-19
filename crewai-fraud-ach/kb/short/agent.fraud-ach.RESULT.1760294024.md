```json
{
  "id": "51b4929e8e582a4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294024,
  "host_pid": "9e6742732c60:1",
  "hash": "ff22e1e47e8f267553d2cbe0b1d05eec696c6ee408e80b588e2a661c080430d3",
  "cid": "QmV1ff22e1e47e8f267553d2cbe0b1d05eec696c6ee4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294024,
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
      "evaluated_at": 1760294024
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
  "sig": "b51a94bbd528ccf4b9097bdc0630ea8bfca4791b13aaad6609c1745d21c47661"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 113631500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}