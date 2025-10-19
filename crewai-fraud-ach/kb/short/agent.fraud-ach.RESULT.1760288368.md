```json
{
  "id": "92a8ab75aea1ec70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288368,
  "host_pid": "9e6742732c60:1",
  "hash": "e690f6decb9cb6362f9756ee09bd00f109861f98f54e3327fb3d729e953938e7",
  "cid": "QmV1e690f6decb9cb6362f9756ee09bd00f109861f98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288368,
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
      "evaluated_at": 1760288368
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
  "sig": "1e1b3fc05ed518c649cbd09a716ceed22c5a1d09983ac8aec547da1605cabd4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241784115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 40945541, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': 'd8ced4219e23835b'}}}