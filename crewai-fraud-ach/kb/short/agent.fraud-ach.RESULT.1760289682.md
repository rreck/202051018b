```json
{
  "id": "a0276cfcfd93a3be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289682,
  "host_pid": "9e6742732c60:1",
  "hash": "fa5adc004c4107e573f5e36585492cc7993809397cb9a7f835171aa48905a241",
  "cid": "QmV1fa5adc004c4107e573f5e36585492cc799380939",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289682,
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
      "evaluated_at": 1760289682
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
  "sig": "155a6520143c0261caa43ca5028a1fe886f4de721c5490c4ab6e577b0df19785"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000023166202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 130000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'ab99b3da8ccd3a17'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}