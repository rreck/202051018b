```json
{
  "id": "07fd2be2ae12e6d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285777,
  "host_pid": "9e6742732c60:1",
  "hash": "6aaf531b5d177378bc1b668a0f721dc17687a450dd9bec2df46e496b14f00bfd",
  "cid": "QmV16aaf531b5d177378bc1b668a0f721dc17687a450",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285777,
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
      "evaluated_at": 1760285777
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
  "sig": "da4dec85d26dc187ccb37e123e782e584f98063ff383fa416df0a48ac270848d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151540950
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9410889}}}