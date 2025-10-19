```json
{
  "id": "74dc2a470ff0183c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289253,
  "host_pid": "9e6742732c60:1",
  "hash": "0e42088272e48b5f01165c86038961e50941a067bd1c88ae29ef3a08132ba426",
  "cid": "QmV10e42088272e48b5f01165c86038961e50941a067",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289253,
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
      "evaluated_at": 1760289253
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
  "sig": "59c030c67079fd568816c3748bdc15299d9056299972f64f7982f6c804f0aabc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024088542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '45759aa393537ed9'}}}