```json
{
  "id": "99970874b066da41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288244,
  "host_pid": "9e6742732c60:1",
  "hash": "cee7e9c90c193e77b9798e3f1fae37954a13f0dbd0ec4e8e0ab41464e5263de4",
  "cid": "QmV1cee7e9c90c193e77b9798e3f1fae37954a13f0db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288244,
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
      "evaluated_at": 1760288244
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
  "sig": "14d5e4eee7cf71a98958ee6d9524beaf3911c9bc492ea773fa6ed440c17bbea8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027276119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 24262560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': 'ec114b5b29b7d5ae'}}}