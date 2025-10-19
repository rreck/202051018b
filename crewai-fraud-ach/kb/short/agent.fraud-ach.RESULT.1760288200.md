```json
{
  "id": "13eea2362b986e3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288200,
  "host_pid": "9e6742732c60:1",
  "hash": "352e1dc52debb2f48d7e002daa23e671cd63b41bbc02c5dcb48d6a2fa8c19c0d",
  "cid": "QmV1352e1dc52debb2f48d7e002daa23e671cd63b41b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288200,
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
      "evaluated_at": 1760288200
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
  "sig": "e073aa97f19f65ae4becf47f1ccd58d6d2cb4994ad27fc48387e9e25efdcbef4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026803563
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 21574132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}