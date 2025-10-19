```json
{
  "id": "d3e43720f99d7b62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293965,
  "host_pid": "9e6742732c60:1",
  "hash": "466e69da95a2dcd76722e608bdcc1b4098157ff188db1f222f6c696f862c408d",
  "cid": "QmV1466e69da95a2dcd76722e608bdcc1b4098157ff1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293965,
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
      "evaluated_at": 1760293965
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
  "sig": "11f7982c6e39f3322201a5a4ea6649b1f9523fd82a0e182493290503a638e45a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023498410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 30294181, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'a97f330737c5e5f9'}}}