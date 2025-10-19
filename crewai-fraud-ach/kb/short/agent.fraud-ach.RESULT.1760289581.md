```json
{
  "id": "2c76011fb228b191",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289581,
  "host_pid": "9e6742732c60:1",
  "hash": "2b739baaec279c4a0852befb800647949caa7ecbf7ff5104ce1e35521f9f1d02",
  "cid": "QmV12b739baaec279c4a0852befb800647949caa7ecb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289581,
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
      "evaluated_at": 1760289581
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
  "sig": "28fc8796a33900a06ebc3843158c616b36ada7242bb475370d0bd903338eeceb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 17880838, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}