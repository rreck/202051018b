```json
{
  "id": "21763b022b339ae0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291414,
  "host_pid": "9e6742732c60:1",
  "hash": "1f5dc6f19433c31fc733aaf5530921019f788941db675ea1b6f45a7df8ce1398",
  "cid": "QmV11f5dc6f19433c31fc733aaf5530921019f788941",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291414,
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
      "evaluated_at": 1760291414
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
  "sig": "00bf5f5d8780be4e1ae710fd07d7d5edf8ad71577cc34c63f36fdb7933e9f57c"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 174000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}