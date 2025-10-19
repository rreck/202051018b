```json
{
  "id": "92a8f7efaf976a98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292199,
  "host_pid": "9e6742732c60:1",
  "hash": "fc1e4481c5aab782e204b0e53d1bc9c6d25b7b37f11e0d6912329ffc15436d1f",
  "cid": "QmV1fc1e4481c5aab782e204b0e53d1bc9c6d25b7b37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292199,
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
      "evaluated_at": 1760292199
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
  "sig": "fa53a6070352ece320e25be5832eb602aabcd25e5baef3961f43caac343a545d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024023598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 51513600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'b47dddaceabbc6a8'}}}