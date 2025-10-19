```json
{
  "id": "182e10486c63675e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289169,
  "host_pid": "9e6742732c60:1",
  "hash": "03c6bc5a0480e4dbaeffdf8b35fc5e670486eabefbea882016683c97bca16693",
  "cid": "QmV103c6bc5a0480e4dbaeffdf8b35fc5e670486eabe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289169,
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
      "evaluated_at": 1760289169
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
  "sig": "ccecbc942eea2eca0e962e577bf164c64f2980d55d2ea0f0f57206d4efcf8237"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 115000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}