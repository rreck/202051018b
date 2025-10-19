```json
{
  "id": "15f40b10fbab9c78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291490,
  "host_pid": "9e6742732c60:1",
  "hash": "9a5745252c684fff5fbe4e081545d863ea0de7624f2d655a3cc4e58010968a6c",
  "cid": "QmV19a5745252c684fff5fbe4e081545d863ea0de762",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291490,
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
      "evaluated_at": 1760291490
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
  "sig": "52a6ab41306c23cd0c1bec65112d6004daf724c28c83dde4833460f14f712855"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270739022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 50790960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '068659374d77a711'}}}