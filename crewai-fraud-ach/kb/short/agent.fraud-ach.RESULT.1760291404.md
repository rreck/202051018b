```json
{
  "id": "861b2009ffc495b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291404,
  "host_pid": "9e6742732c60:1",
  "hash": "b31128703d944ac2c07f73b48925fb9750550d4d09b578ce3d9740eec2b82269",
  "cid": "QmV1b31128703d944ac2c07f73b48925fb9750550d4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291404,
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
      "evaluated_at": 1760291404
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
  "sig": "4541c8521b99d2b39868da17fca533ed35679945c6ef7c70c5df07c87364f595"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460804941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 12824496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'e3b2eb0d41697d4a'}}}