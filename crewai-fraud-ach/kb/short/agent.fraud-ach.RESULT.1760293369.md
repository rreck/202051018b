```json
{
  "id": "979a18f74a7a6635",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293369,
  "host_pid": "9e6742732c60:1",
  "hash": "04526d82ad9f2ab26295e1dfde9baab2a7e9ff65ea977605da691f004cb67381",
  "cid": "QmV104526d82ad9f2ab26295e1dfde9baab2a7e9ff65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293369,
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
      "evaluated_at": 1760293369
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
  "sig": "d8a35f89ddb0260c8f7d08d9cec64fadbdcbcd037920455c36c9a99f12863149"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 021000020489818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 1830422125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': 'b3efe19f99a87213'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}