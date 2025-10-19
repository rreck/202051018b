```json
{
  "id": "0f6858ef976c41c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288423,
  "host_pid": "9e6742732c60:1",
  "hash": "d7cc7c7362b179a450e5d0e927c25a4b162412f74aaa636d9ae87a9e798e4488",
  "cid": "QmV1d7cc7c7362b179a450e5d0e927c25a4b162412f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288423,
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
      "evaluated_at": 1760288423
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
  "sig": "3b1c7b267164cb53eeac0721830e8d30b48d927429be3544feb09ae6c784c1c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466882033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 27861126, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': '7e4548b1f8f2bba3'}}}