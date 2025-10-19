```json
{
  "id": "98f34c620d7606ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293532,
  "host_pid": "9e6742732c60:1",
  "hash": "c1adfb55e58cb03f15cac95a258e37155ef3335e3641854f81b8b6926c82a107",
  "cid": "QmV1c1adfb55e58cb03f15cac95a258e37155ef3335e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293532,
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
      "evaluated_at": 1760293532
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
  "sig": "816bcf4e7dacc38785ea90cf09292477ad976a6a2b52f7c4df7fc29a3cb1e63e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 98581780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}