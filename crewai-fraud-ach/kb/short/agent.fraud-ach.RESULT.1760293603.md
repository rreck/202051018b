```json
{
  "id": "16a95a015d4c9a07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293603,
  "host_pid": "9e6742732c60:1",
  "hash": "027f347f06a0a9a570dee2673d04e410a258fb06e2751f54f4eb099fdebf6360",
  "cid": "QmV1027f347f06a0a9a570dee2673d04e410a258fb06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293603,
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
      "evaluated_at": 1760293603
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
  "sig": "5e488c35dd48591b43e1857ab415fcb4abef1cce4a8df1b7ff95a74eb9b2d2b9"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000029533260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 1780117878, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '6cc2b71c57585513'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018549}}}