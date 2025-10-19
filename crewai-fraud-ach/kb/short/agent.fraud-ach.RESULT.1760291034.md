```json
{
  "id": "957becb8da591bd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291034,
  "host_pid": "9e6742732c60:1",
  "hash": "e86f9694a967eb7668734c3e351ba56d5cbbae2cdab9be3d282e60d77748ff15",
  "cid": "QmV1e86f9694a967eb7668734c3e351ba56d5cbbae2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291034,
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
      "evaluated_at": 1760291034
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
  "sig": "ac0bc45730f86005828e84332d1f843ada29ff6e600ca02b675f39940866d6e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159090424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 28534605, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': 'fe78f8ea626833d8'}}}