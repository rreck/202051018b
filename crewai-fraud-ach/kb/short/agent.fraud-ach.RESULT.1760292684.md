```json
{
  "id": "f104f6248c240d1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292684,
  "host_pid": "9e6742732c60:1",
  "hash": "272aa35ee24e45a7b6cb7c62dfddee9c673e2221eafbb123b53802dc864bd449",
  "cid": "QmV1272aa35ee24e45a7b6cb7c62dfddee9c673e2221",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292684,
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
      "evaluated_at": 1760292684
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
  "sig": "3d7241ed8f72027983256bb9d738389e433ca3f12d6c10d50b9bd879b5e1c0db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038072034
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 70854917, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '336ae1a1ad6e821c'}}}