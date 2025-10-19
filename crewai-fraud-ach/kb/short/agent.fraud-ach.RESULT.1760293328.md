```json
{
  "id": "0e533026dc8ae649",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293328,
  "host_pid": "9e6742732c60:1",
  "hash": "ff7ed2c53df92d2c377fc5c7bc1b291122234ac0f64d4c6ca17e68a9c42b7713",
  "cid": "QmV1ff7ed2c53df92d2c377fc5c7bc1b291122234ac0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293328,
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
      "evaluated_at": 1760293328
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
  "sig": "627d52a29d24c31f4f1d5c4013f1130cb076673cdf5e9b2a4419f8d6b970cd15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 292, 'threshold': 50, 'total_amount': 24342580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 291, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}}