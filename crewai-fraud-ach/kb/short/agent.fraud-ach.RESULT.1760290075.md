```json
{
  "id": "f1f2fc11e90bd662",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290075,
  "host_pid": "9e6742732c60:1",
  "hash": "ac3ce1b9ee3fdaacb17adcf94e693d0de72402925cfc2fe48428b58c2e824f31",
  "cid": "QmV1ac3ce1b9ee3fdaacb17adcf94e693d0de7240292",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290075,
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
      "evaluated_at": 1760290075
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
  "sig": "43443dd2e1989e4c401fbf71cbdf58042004b6f8204fafab3307fa7d0c12612e"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463734572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 70500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '9877b0a7b07093eb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}57577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6664302}}}