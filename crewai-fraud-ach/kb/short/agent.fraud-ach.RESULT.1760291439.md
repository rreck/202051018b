```json
{
  "id": "1cc295f7fb748198",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291439,
  "host_pid": "9e6742732c60:1",
  "hash": "328199a0f821a9241076bb3f984691fb130552696fa605315d7ed37ea6c15139",
  "cid": "QmV1328199a0f821a9241076bb3f984691fb13055269",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291439,
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
      "evaluated_at": 1760291439
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
  "sig": "189579ab0aed0d258bd1b9617ca4c37280f9e6c259e142881ac954253e71b672"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024762963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 17500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285764, 'matching_hash': 'dd3a0eba0797b423'}}}