```json
{
  "id": "7d12623cbce84525",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287864,
  "host_pid": "9e6742732c60:1",
  "hash": "d6bb0372a0b2bc7b894d4b69c6c1cc7a24bb6021c2a088116a5eb68e83337581",
  "cid": "QmV1d6bb0372a0b2bc7b894d4b69c6c1cc7a24bb6021",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287864,
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
      "evaluated_at": 1760287864
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
  "sig": "ea07c537bc91c3ba3d61ca69141aa402263f2c23a7230d6e04846b4203c26063"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 063100279773830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 37500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': '49e9eab15cee1f0f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}