```json
{
  "id": "b9818aea2f21814f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289293,
  "host_pid": "9e6742732c60:1",
  "hash": "c11141d6cbd4dfbb00523d32110b5787cd66dac8bdf291baa87daf74bf1474b2",
  "cid": "QmV1c11141d6cbd4dfbb00523d32110b5787cd66dac8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289293,
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
      "evaluated_at": 1760289293
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
  "sig": "6da60fe0be316749e48f6196c3225e2713a3b6f3121d65114c687a781f0f0b0b"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201462613659
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 735233408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': '5c1e39699924121a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6178432}}}