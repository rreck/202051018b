```json
{
  "id": "83770a2118cb4b04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294589,
  "host_pid": "9e6742732c60:1",
  "hash": "aaf28c703eb8d8e88ae3d71fec3010522e60676786e963f5b5f18bd943fa20c1",
  "cid": "QmV1aaf28c703eb8d8e88ae3d71fec3010522e606767",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294589,
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
      "evaluated_at": 1760294589
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
  "sig": "b6fbf1cbe0cb6504efab8f6b7ae3de7e3eb89af60eb54d46cb3e3f2fdb45f086"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 62597581, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}