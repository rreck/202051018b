```json
{
  "id": "8b797e322092f6e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286551,
  "host_pid": "9e6742732c60:1",
  "hash": "e064acae94f2922df56d08fb39fde83eddd7f6a17c9c8abb1e2c9357f986dd8d",
  "cid": "QmV1e064acae94f2922df56d08fb39fde83eddd7f6a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286551,
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
      "evaluated_at": 1760286551
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
  "sig": "551f5696eda8f558c9d59093ad15313a0ae3377f9758bf2ef6aa1c65ddb5f6c2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240945799
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}re': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6178432}}}