```json
{
  "id": "0f3606e5ca7e7055",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293891,
  "host_pid": "9e6742732c60:1",
  "hash": "ee73b7bcab30465c03e3abb1725a76b044bc77fd4987d0ffa2de709bce72ecc2",
  "cid": "QmV1ee73b7bcab30465c03e3abb1725a76b044bc77fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293891,
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
      "evaluated_at": 1760293891
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
  "sig": "e999f2c72299e1be946e170ec8be523cb8bb44fc4ae8de40d84a050c7536b3b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 95690034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}