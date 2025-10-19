```json
{
  "id": "619411da76a29192",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292200,
  "host_pid": "9e6742732c60:1",
  "hash": "e685d195c26999be75d80bb5286c493f340f13ee3ed9a5853dd987919b2b62f3",
  "cid": "QmV1e685d195c26999be75d80bb5286c493f340f13ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292200,
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
      "evaluated_at": 1760292200
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
  "sig": "4654439042087daa1cf86b66e916d39b99b1beda40d80b0d5dd15e0183dd69e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021005824
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}