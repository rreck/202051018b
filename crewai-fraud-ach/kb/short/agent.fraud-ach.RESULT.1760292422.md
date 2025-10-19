```json
{
  "id": "a2dbb3bc2b53c3aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292422,
  "host_pid": "9e6742732c60:1",
  "hash": "f2c7107f2f568e5c54be3cdfd6c133b2d15e4e5fc3a112ff5c10197eb1590c96",
  "cid": "QmV1f2c7107f2f568e5c54be3cdfd6c133b2d15e4e5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292422,
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
      "evaluated_at": 1760292422
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
  "sig": "93eaca280aee6ed9e17471d7e81bbf01c74702e25f9015e3a61e1180fae14a84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246900677
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 273, 'threshold': 50, 'total_amount': 118597206, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 272, 'first_seen': 1760284979, 'matching_hash': '3c9e668125e5b467'}}}