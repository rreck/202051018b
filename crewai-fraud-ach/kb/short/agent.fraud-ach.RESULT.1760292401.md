```json
{
  "id": "6e5513a5eef7e757",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292401,
  "host_pid": "9e6742732c60:1",
  "hash": "0977e273f62b82fa3c06daa5e180e03e6b3f0dc2e05bc82b53603d4002fd6aa3",
  "cid": "QmV10977e273f62b82fa3c06daa5e180e03e6b3f0dc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292401,
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
      "evaluated_at": 1760292401
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
  "sig": "327192fd1293283ece275fefd1b8026c1de051268e6c91fe459189da8fb999e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029996971
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 20490561, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '92fd98aa1089d1f1'}}}