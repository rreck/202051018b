```json
{
  "id": "05bc6ebc56820fdf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288658,
  "host_pid": "9e6742732c60:1",
  "hash": "a988a9a040702e0b754d411d4fbbd226bc19cae1dc52c7f16840f9962ae5f947",
  "cid": "QmV1a988a9a040702e0b754d411d4fbbd226bc19cae1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288658,
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
      "evaluated_at": 1760288658
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
  "sig": "0fc12c244d1f33002e9a4034d39ee440e1bde343a8fda1c2d97093e820393d73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279947961
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '22db2c62b181c93f'}}}een': 1760285763, 'matching_hash': 'aef06f437446325c'}}}