```json
{
  "id": "806c2740e70f880f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288280,
  "host_pid": "9e6742732c60:1",
  "hash": "26fb9aea7276b31dd570282ac92fa2c67c01adeb4cd96c85431b1cc9eea8d548",
  "cid": "QmV126fb9aea7276b31dd570282ac92fa2c67c01adeb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288280,
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
      "evaluated_at": 1760288280
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
  "sig": "08c4a4ae25ba0875e021185bf98b0784d0832454621aeb4c24b13339e244ca66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}