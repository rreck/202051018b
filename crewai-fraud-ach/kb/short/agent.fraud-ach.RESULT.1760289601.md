```json
{
  "id": "ec7af4074ac85d19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289601,
  "host_pid": "9e6742732c60:1",
  "hash": "64b9aad10f999c1703fca91902f738642b66b0b913e4011fa0ce6c110a7508ec",
  "cid": "QmV164b9aad10f999c1703fca91902f738642b66b0b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289601,
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
      "evaluated_at": 1760289601
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
  "sig": "4427de0f32ecef81d2c57499c8b3fae6df44c5dcd5ae0fb393095460056a82c9"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000029533260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 1026374272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018549}}}