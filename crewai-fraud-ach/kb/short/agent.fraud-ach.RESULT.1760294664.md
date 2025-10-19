```json
{
  "id": "3959a65fa25d1bbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294664,
  "host_pid": "9e6742732c60:1",
  "hash": "a3edd1d5f6fdc5ade4a1e697dd1732be623a491a5a38f6cd7d74f1fb45c1ac37",
  "cid": "QmV1a3edd1d5f6fdc5ade4a1e697dd1732be623a491a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294664,
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
      "evaluated_at": 1760294664
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
  "sig": "7b0aea13e13c6b5d5032638f496ec337e86b2734bd5d4b5b5134ad070fa8a80b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 64472914, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}