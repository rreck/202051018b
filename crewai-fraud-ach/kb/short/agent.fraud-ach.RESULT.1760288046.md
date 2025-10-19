```json
{
  "id": "1f1cc2dfc3053917",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288046,
  "host_pid": "9e6742732c60:1",
  "hash": "081f88f43b4e79ee5e285fc2a5623311f18a31869a955e5bceae4de400d1e95c",
  "cid": "QmV1081f88f43b4e79ee5e285fc2a5623311f18a3186",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288046,
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
      "evaluated_at": 1760288046
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
  "sig": "41a08deda44b44bdd80e0675a5390a9b74cad9d2ba79b03bab5de038259afde3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038073979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': '05e8b4bb68b88ac5'}}}