```json
{
  "id": "ac69bfb62a624b66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290976,
  "host_pid": "9e6742732c60:1",
  "hash": "9cc840a0d7b273bb222fd40bd10202bf01258aee615e2cfe888a7d41917e9735",
  "cid": "QmV19cc840a0d7b273bb222fd40bd10202bf01258aee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290976,
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
      "evaluated_at": 1760290976
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
  "sig": "098aac8b169778f9de79b2ce60f478c97675be44ba0bbb55f69111f1e321eb56"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 026009595171446
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 1062463176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '6f6a57bfd56698c7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6478434}}}