```json
{
  "id": "c7551fcf1ddb7316",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290250,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b63ec29ba670b19b992294bd8c32d9078c4a84c8ab9138e111ba57e9c8bde2",
  "cid": "QmV1e4b63ec29ba670b19b992294bd8c32d9078c4a84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290250,
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
      "evaluated_at": 1760290250
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
  "sig": "6e818916d95eaaf0fc6d61c9bc93d3df7033426026349e6aee23d5dcf7ad2cc4"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 145000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}