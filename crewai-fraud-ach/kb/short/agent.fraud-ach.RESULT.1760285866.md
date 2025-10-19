```json
{
  "id": "993a6748c91cbc89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285866,
  "host_pid": "9e6742732c60:1",
  "hash": "a0f102e601c7baaa928beb80f802b9edfb538505766fceae7228424cc9a77e14",
  "cid": "QmV1a0f102e601c7baaa928beb80f802b9edfb538505",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285866,
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
      "evaluated_at": 1760285866
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
  "sig": "c21b96bfe73205d0fda18008c5329d1c210488cf4dbf8051259f9a987f57757e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105159207469
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': '9ea174210fc0f6af'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}