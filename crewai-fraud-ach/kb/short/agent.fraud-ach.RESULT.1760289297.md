```json
{
  "id": "e85fc6a84d21c30c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289297,
  "host_pid": "9e6742732c60:1",
  "hash": "f01942ae2a3da55a2d2f9db22df8d341cc7bbce8fd09d1b00777172dd15cfaee",
  "cid": "QmV1f01942ae2a3da55a2d2f9db22df8d341cc7bbce8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289297,
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
      "evaluated_at": 1760289297
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
  "sig": "197f366d82908231523eb4859d44345c83a732ea3ec09ae2f9f53dd537db490c"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000029388663
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 1910124450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760284979, 'matching_hash': '503d742180c16441'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9795510}}}