```json
{
  "id": "b57af2747dca978d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291582,
  "host_pid": "9e6742732c60:1",
  "hash": "1ab5fde2cc7eae7d04109e6a24bbd4214bc9d520a04633ea9342f7f831911f74",
  "cid": "QmV11ab5fde2cc7eae7d04109e6a24bbd4214bc9d520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291582,
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
      "evaluated_at": 1760291582
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
  "sig": "b653c45928ed069851cbdba395d1cc84ed4179ea95eab27bb82987116a194b50"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243340063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 75450996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '5f2724e98c8a67b0'}}}