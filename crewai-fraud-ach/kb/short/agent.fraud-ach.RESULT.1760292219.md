```json
{
  "id": "2b61d5e066f709a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292219,
  "host_pid": "9e6742732c60:1",
  "hash": "993361fb553283af8366cffb8fddc82b345e46f2f6feec5ed8f7bf3e0a3e92c7",
  "cid": "QmV1993361fb553283af8366cffb8fddc82b345e46f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292219,
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
      "evaluated_at": 1760292219
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "56f3224e7ed0bd2263c944be3d1cd5f711e21179c6b85874b3aa6da1f83c53b2"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028645436
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 96500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '6242cc5f185f73d7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}