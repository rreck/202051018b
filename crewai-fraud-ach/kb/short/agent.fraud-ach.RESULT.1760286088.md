```json
{
  "id": "3634db2fb6c2c346",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286088,
  "host_pid": "9e6742732c60:1",
  "hash": "30426d566364a3c49e8c3494b3b5e127d05ee4444ea612d0f342310ea6cb50b4",
  "cid": "QmV130426d566364a3c49e8c3494b3b5e127d05ee444",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286088,
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
      "evaluated_at": 1760286088
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
  "sig": "be35f3e88d9070da6d1e6fae3e055bf101b3755dbc2a471440494fcd0c81dab7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248569332
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}