```json
{
  "id": "0fcc90e832eada89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285845,
  "host_pid": "9e6742732c60:1",
  "hash": "db142c5898c2eaa92a17a936165925d97b8cfead7aeaa57afcb25f66e6115792",
  "cid": "QmV1db142c5898c2eaa92a17a936165925d97b8cfead",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285845,
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
      "evaluated_at": 1760285845
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
  "sig": "3cbd436804034f44eb7b778f8be3d9d5be3d0d76bec5dff34d32301c6a91f224"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 031201467886368
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285763, 'matching_hash': 'b8e6d176a4768585'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5513113}}}