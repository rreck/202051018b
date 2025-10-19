```json
{
  "id": "cbd88e795881306a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286793,
  "host_pid": "9e6742732c60:1",
  "hash": "55a919c5b2f64a63ddeef3e2e8eadaf9a13b9c0fb47d7f5662f831b587ea0801",
  "cid": "QmV155a919c5b2f64a63ddeef3e2e8eadaf9a13b9c0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286793,
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
      "evaluated_at": 1760286793
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "fc413b71adf5931d1d857753d31288b3417f14b1786a678a3997f9cf6cbb437e"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 121000241325245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 301907235, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': '97920a0a35eda98b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.02, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8159655}}}