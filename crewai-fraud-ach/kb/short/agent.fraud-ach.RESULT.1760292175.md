```json
{
  "id": "5f1cad76bf43f846",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292175,
  "host_pid": "9e6742732c60:1",
  "hash": "21b6bd0083e03e1c3b19806787dede650f416a6e04d01dc45dd3f406b3bc4ee6",
  "cid": "QmV121b6bd0083e03e1c3b19806787dede650f416a6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292175,
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
      "evaluated_at": 1760292175
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
  "sig": "baaa8ae3b8bcb9eff47b1e77d3ecb6b204c271a72f8f6a01726f369edf78e6c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025810032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 94033728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '4a1b4df87be22a11'}}}