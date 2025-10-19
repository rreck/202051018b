```json
{
  "id": "17d96b3467de16ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293981,
  "host_pid": "9e6742732c60:1",
  "hash": "e7cacf5a9726d9857e763bc7168a586d4e392be1c43bee9e145462a40a0ebc41",
  "cid": "QmV1e7cacf5a9726d9857e763bc7168a586d4e392be1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293981,
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
      "evaluated_at": 1760293981
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
  "sig": "b1839c1be3570781b1e7f372694f604c07fa56840c7c26f3abf2abd504352f08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028775289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 305, 'threshold': 50, 'total_amount': 113610365, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 304, 'first_seen': 1760284979, 'matching_hash': 'c3a7255fa6117479'}}}