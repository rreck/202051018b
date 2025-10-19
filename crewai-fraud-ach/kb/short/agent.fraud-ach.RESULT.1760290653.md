```json
{
  "id": "fe7854e71d7d9caa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290653,
  "host_pid": "9e6742732c60:1",
  "hash": "ad096fa3651aa14cda1d046ee7d18dd92cfa40bfa9e41fc7f8160488a4942ec0",
  "cid": "QmV1ad096fa3651aa14cda1d046ee7d18dd92cfa40bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290653,
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
      "evaluated_at": 1760290653
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "492754313da9f1550bc0ddda572415ba2ec10e61f7a87b5887bf67e7cd97d567"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464768410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 73014552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '182aec6491bb83ab'}}}maly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.66, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7156929}}}