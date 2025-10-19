```json
{
  "id": "44807d1ee3311ac4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293821,
  "host_pid": "9e6742732c60:1",
  "hash": "3f67ea188ea9def0aee33923b925c1e0ef11eff20f9e7fbda533d20eea1532d3",
  "cid": "QmV13f67ea188ea9def0aee33923b925c1e0ef11eff2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293821,
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
      "evaluated_at": 1760293821
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
  "sig": "e94670c62d09cc6a54698486c7f2c3f7088aa6936ed499509e4d8681d3f96762"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243890645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 41153470, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}}