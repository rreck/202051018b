```json
{
  "id": "6ef9f2bb71bf20b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288422,
  "host_pid": "9e6742732c60:1",
  "hash": "4571c9c23a839ec8d120c526d6a6e1c3ea52853aa382af266ee872c3d6fabcca",
  "cid": "QmV14571c9c23a839ec8d120c526d6a6e1c3ea52853a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288422,
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
      "evaluated_at": 1760288422
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
  "sig": "e0fa37d0a458a77a67007fdea3d463e25736ba0505e109e9ae9d8a901501016e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 33466329, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}