```json
{
  "id": "dcf55f7f5849ae90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292621,
  "host_pid": "9e6742732c60:1",
  "hash": "a94506d40c6b4aa317b6188834e70ba9dbe82d5a0b68312001eb5d7067a41d29",
  "cid": "QmV1a94506d40c6b4aa317b6188834e70ba9dbe82d5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292621,
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
      "evaluated_at": 1760292621
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
  "sig": "f54eea6cee4dc38410c38c78e0758e2a54b5c8c214680391ccaa5192c526980d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 42190704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}