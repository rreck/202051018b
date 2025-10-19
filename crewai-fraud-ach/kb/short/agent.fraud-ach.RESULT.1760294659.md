```json
{
  "id": "016ad6464387f0a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294659,
  "host_pid": "9e6742732c60:1",
  "hash": "28365bee6bb0780d22a0d855e350959f6cc105c06d4dc42d3bedc895fc30f221",
  "cid": "QmV128365bee6bb0780d22a0d855e350959f6cc105c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294659,
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
      "evaluated_at": 1760294659
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
  "sig": "386ecda14d38d0149ef7211eed808e9ad16b313ec8c9aaf494774b31f4d9db1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591582850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 80001086, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '5102e2097242c74b'}}}