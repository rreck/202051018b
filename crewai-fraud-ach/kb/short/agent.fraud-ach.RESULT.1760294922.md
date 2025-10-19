```json
{
  "id": "499766f9005b5d57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294922,
  "host_pid": "9e6742732c60:1",
  "hash": "e3d3b90934a388e23b01e8f988ac4618fa866331df0c7bc6ef79975917b56107",
  "cid": "QmV1e3d3b90934a388e23b01e8f988ac4618fa866331",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294922,
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
      "evaluated_at": 1760294922
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
  "sig": "4110eb1319aa4c3b8aa861492610d677e7be53ac228a94b22c7c2e7ebf407edb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 20408375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}