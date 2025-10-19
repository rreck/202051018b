```json
{
  "id": "7d24f87497e80844",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289833,
  "host_pid": "9e6742732c60:1",
  "hash": "fd54974804d97ffc408e92d126653906a35840fe2c91f30d4c5725f949193437",
  "cid": "QmV1fd54974804d97ffc408e92d126653906a35840fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289833,
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
      "evaluated_at": 1760289833
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
  "sig": "3a832cd787f40ff33b0e2ae65341121dc756cb3946867ad734409670dd4cae0d"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 134000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}