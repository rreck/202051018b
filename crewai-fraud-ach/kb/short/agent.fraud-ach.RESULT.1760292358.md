```json
{
  "id": "cc9b082e5506377e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292358,
  "host_pid": "9e6742732c60:1",
  "hash": "098702bd415bf3fa5d0e73b7a0f56621ae219414123c28da60539985585c17ac",
  "cid": "QmV1098702bd415bf3fa5d0e73b7a0f56621ae219414",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292358,
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
      "evaluated_at": 1760292358
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
  "sig": "e2d9efaf73046e731adc795703326aef222bff02ba2a36b41ecd5ac72a95f91f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 83297060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}