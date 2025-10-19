```json
{
  "id": "050988d5148d6a6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293133,
  "host_pid": "9e6742732c60:1",
  "hash": "d9ee8e77359b75cd9b5848f8fd6a3dd87170ff73dc46cbec9a4cead2fbc9393b",
  "cid": "QmV1d9ee8e77359b75cd9b5848f8fd6a3dd87170ff73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293133,
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
      "evaluated_at": 1760293133
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
  "sig": "8a6d93e6a829f3b5bc824049442ac3ba27ee64ae34e7ceffcc89b5c7e6f0b76d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592366893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 64874968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285764, 'matching_hash': '065c48a9e05564fe'}}}maly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5595688}}}