```json
{
  "id": "d50f0faf56f7adc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286308,
  "host_pid": "9e6742732c60:1",
  "hash": "057a87d26a5f7c93944e60211aba84caeaf0fb96b5ba59c6060152de3bf12e10",
  "cid": "QmV1057a87d26a5f7c93944e60211aba84caeaf0fb96",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286308,
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
      "evaluated_at": 1760286308
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
  "sig": "74b35dc70a8c5eb085f209d7c1d888617cf4ece734bb234e23b5c96de1152991"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029163318
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}