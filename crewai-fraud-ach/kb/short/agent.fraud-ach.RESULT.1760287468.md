```json
{
  "id": "7cba85634f6a7d01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287468,
  "host_pid": "9e6742732c60:1",
  "hash": "97ac89cd981dc3a2bc97d43f67ed753fd9f227ac0aa66117e9247ff6e4a2316e",
  "cid": "QmV197ac89cd981dc3a2bc97d43f67ed753fd9f227ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287468,
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
      "evaluated_at": 1760287468
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
  "sig": "ae00a1df8e74cf425e14d82285542befaa31c2026c51d655afab6481a4c4bb57"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 567672466, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.53, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306106}}}