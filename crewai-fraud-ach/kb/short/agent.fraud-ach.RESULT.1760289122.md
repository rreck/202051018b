```json
{
  "id": "cb0ba9624e73734d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289122,
  "host_pid": "9e6742732c60:1",
  "hash": "3dc27b3df4b81677b5b122196deb8cf3d652e7148d04f65be1ea9f5568733fce",
  "cid": "QmV13dc27b3df4b81677b5b122196deb8cf3d652e714",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289122,
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
      "evaluated_at": 1760289122
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
  "sig": "2b6fff7defa7356b1d7f0be0ab9c9345b121a3f9f405ff16ebf5918ccb22eba0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270124106
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 47201244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '785cd1c2415b19ab'}}}