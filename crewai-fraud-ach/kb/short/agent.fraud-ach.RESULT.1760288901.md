```json
{
  "id": "53c72804ea897900",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288901,
  "host_pid": "9e6742732c60:1",
  "hash": "ce7474d8bbc8f8fd32f6116ebeb9bfa79a9611b087019b8844652139d7128ff8",
  "cid": "QmV1ce7474d8bbc8f8fd32f6116ebeb9bfa79a9611b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288901,
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
      "evaluated_at": 1760288901
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
  "sig": "7bb2d3da8c9f0e3a1e6bbda00d2470131984994f90edd42f0f702c0b551b8821"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 27846964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}