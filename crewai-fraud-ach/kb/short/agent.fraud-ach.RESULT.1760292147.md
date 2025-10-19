```json
{
  "id": "0b708469c2110503",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292147,
  "host_pid": "9e6742732c60:1",
  "hash": "0849765fac72594d2d162b7d9a248fdd10473c1ff13dd0f0e20f1f1a495b1dc3",
  "cid": "QmV10849765fac72594d2d162b7d9a248fdd10473c1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292147,
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
      "evaluated_at": 1760292147
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
  "sig": "26f82581dd22b96fc20e3c097c5ccbf5714fc55f36747b83f7cce43c5056298c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591685004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 62812642, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}