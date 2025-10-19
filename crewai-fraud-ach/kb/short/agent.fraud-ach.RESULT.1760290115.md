```json
{
  "id": "91121b48c6c3f86f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290115,
  "host_pid": "9e6742732c60:1",
  "hash": "7f69f55aeff27c2ca00475a096f118e4d2a9b9c95ead7ac89a38f70b34979b7b",
  "cid": "QmV17f69f55aeff27c2ca00475a096f118e4d2a9b9c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290115,
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
      "evaluated_at": 1760290115
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
  "sig": "e689cb552f392680b6b3dacad6982bf6ba2a47695eb388f77c34f8983c67692d"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100277197484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 1412529096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '4232e93b8d4c62d2'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9947388}}}