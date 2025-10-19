```json
{
  "id": "4f8618cc9c7b32f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289645,
  "host_pid": "9e6742732c60:1",
  "hash": "6fbb582892723b65b5414c4356eb8fb3cec6e336bc1a9866ee2a407c267f3d50",
  "cid": "QmV16fbb582892723b65b5414c4356eb8fb3cec6e336",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289645,
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
      "evaluated_at": 1760289645
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
  "sig": "0effdfafd65478ee739489b60c66c9f608fab75be2a1de7587975fbafa547fc7"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463963144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 64500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '4b7135c5b7384c49'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}