```json
{
  "id": "47222a0900f12005",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294063,
  "host_pid": "9e6742732c60:1",
  "hash": "ab6ef71fd0994d2337bc545d59b96f5057475a8ff0dab6ed7d34d25933b1200d",
  "cid": "QmV1ab6ef71fd0994d2337bc545d59b96f5057475a8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294063,
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
      "evaluated_at": 1760294063
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
  "sig": "ce5c52863224b9a2c8b2e1b8a4d3db8385ccc6d5cb52814e8348050bf7b3e4f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592351032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 48708891, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7694908}}}