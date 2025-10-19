```json
{
  "id": "330c4e0211c8ce72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293960,
  "host_pid": "9e6742732c60:1",
  "hash": "f53eb7a8456718f2fabbe56a6e7609218e5021dcc36fb07788ecfc86e6da2209",
  "cid": "QmV1f53eb7a8456718f2fabbe56a6e7609218e5021dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293960,
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
      "evaluated_at": 1760293960
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
  "sig": "172addc96a702ab9971c2eff9d4ca6d2e07f7b191154e104226fc895723764c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 101181589, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}