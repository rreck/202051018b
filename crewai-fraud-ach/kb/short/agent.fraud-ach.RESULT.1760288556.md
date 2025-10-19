```json
{
  "id": "d697571ffcefac91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288556,
  "host_pid": "9e6742732c60:1",
  "hash": "ffbe607e9504643f4e691b4ff74644c49f9fee9a56bbfd86351a102ffc4eb25c",
  "cid": "QmV1ffbe607e9504643f4e691b4ff74644c49f9fee9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288556,
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
      "evaluated_at": 1760288556
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
  "sig": "c5a801fc29c24e744aede6a94af4813fc8af2345d9c84672d0ae693b17bfe218"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 10549041, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}