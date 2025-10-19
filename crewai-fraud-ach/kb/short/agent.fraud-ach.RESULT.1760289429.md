```json
{
  "id": "d5d259e48c9a9470",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289429,
  "host_pid": "9e6742732c60:1",
  "hash": "baa3325818adeabd7ad78aea9f99cfe681c04de3f1045cb2df6bd3a4f9f797a8",
  "cid": "QmV1baa3325818adeabd7ad78aea9f99cfe681c04de3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289429,
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
      "evaluated_at": 1760289429
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
  "sig": "c30fc49eb0cc236cdd5047a6db7c4c5bcebde169d2a9fa46d33efddfea28b00c"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009593536261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 847299522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285764, 'matching_hash': 'ca8349fc21f82b4d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6888614}}}