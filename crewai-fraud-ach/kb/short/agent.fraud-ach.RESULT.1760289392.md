```json
{
  "id": "d58f5252ccf71c31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289392,
  "host_pid": "9e6742732c60:1",
  "hash": "05bdf0978f8cb80c0b1b5f7ccf727c3a5c3081c6872e82ce50f79e3f309b4609",
  "cid": "QmV105bdf0978f8cb80c0b1b5f7ccf727c3a5c3081c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289392,
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
      "evaluated_at": 1760289392
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
  "sig": "a78c65c3c0fb06424e4904960643acf30d68090a959ea48edf11ab3fe8d36bf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461090276
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 31615080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '697ecd0ef10c625b'}}}