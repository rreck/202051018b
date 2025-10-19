```json
{
  "id": "ab39a07dcb6267b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289786,
  "host_pid": "9e6742732c60:1",
  "hash": "ab03b1091acdd10d7d176dae4c28b054e6af63ca47615de9298849d88b9202f9",
  "cid": "QmV1ab03b1091acdd10d7d176dae4c28b054e6af63ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289786,
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
      "evaluated_at": 1760289786
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "993f37fc2f03364239fee3154c422208d882259ce4fba25e5f458cdad0d56eeb"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 866022185, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6511445}}}