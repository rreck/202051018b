```json
{
  "id": "3c4b17dad62ec83f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291282,
  "host_pid": "9e6742732c60:1",
  "hash": "6710ab2c8aca33419fbc6b6c914182eca4c25540b988405d4ad6bf35f416aa79",
  "cid": "QmV16710ab2c8aca33419fbc6b6c914182eca4c25540",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291282,
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
      "evaluated_at": 1760291282
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
  "sig": "6c484088485a1cbcfb56b7ff2d5066a9b8cbd8d9f15ba357146acd8aa099534a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 64948023, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}