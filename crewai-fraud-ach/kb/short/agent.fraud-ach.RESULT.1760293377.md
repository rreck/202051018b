```json
{
  "id": "5f57c11d98a8e548",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293377,
  "host_pid": "9e6742732c60:1",
  "hash": "4d66903b1cd94d26adf6a5d4a9735410e804097cc4e5a8cb147259c982ae53d3",
  "cid": "QmV14d66903b1cd94d26adf6a5d4a9735410e804097c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293377,
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
      "evaluated_at": 1760293377
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
  "sig": "adf36c75719b3f98666d5ec29ef56658c51b77f86956928c955e20178acd098e"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 293, 'threshold': 50, 'total_amount': 2870084430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 292, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9795510}}}