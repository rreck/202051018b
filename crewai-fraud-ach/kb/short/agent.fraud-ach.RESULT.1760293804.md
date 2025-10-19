```json
{
  "id": "374d51674473e402",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293804,
  "host_pid": "9e6742732c60:1",
  "hash": "11dc0b91eed912011d82efdaa7937eec112cf4ea45ece7feab7cca04225c4a33",
  "cid": "QmV111dc0b91eed912011d82efdaa7937eec112cf4ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293804,
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
      "evaluated_at": 1760293804
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
  "sig": "b9db7b27592fce736cfcef5a113f33ada053037674a37799bc64cff7a3f3e407"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 063100273161862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 226000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '7792cb8eb05ccf8f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}