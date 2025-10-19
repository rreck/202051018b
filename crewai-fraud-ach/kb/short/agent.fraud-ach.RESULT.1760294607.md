```json
{
  "id": "0418d2dab3f1c2cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294607,
  "host_pid": "9e6742732c60:1",
  "hash": "cfb1c136ed2a19e940870f2cc7201c349a1faca3b2c7fc99b242cb8eea445286",
  "cid": "QmV1cfb1c136ed2a19e940870f2cc7201c349a1faca3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294607,
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
      "evaluated_at": 1760294607
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
  "sig": "e6f5791c12b99c6de902db41b1699f8806eef33e1de6d3eb5c8a0e1ed634e1aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 119066050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}