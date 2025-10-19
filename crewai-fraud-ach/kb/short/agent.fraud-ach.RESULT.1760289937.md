```json
{
  "id": "6b63ec11366e7dbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289937,
  "host_pid": "9e6742732c60:1",
  "hash": "770b8d3c7116409886c710995004cec3e8f88bdb6fd0f4ee8a58583f5d3e2fb2",
  "cid": "QmV1770b8d3c7116409886c710995004cec3e8f88bdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289937,
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
      "evaluated_at": 1760289937
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
  "sig": "870168a8d1cb42dcc23545c43a85a26b116e06bcb94ac8757f0c3ab3acb079c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271730017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 49975408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '5b0cb81735d50318'}}}