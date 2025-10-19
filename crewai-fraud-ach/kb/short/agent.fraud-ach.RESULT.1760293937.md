```json
{
  "id": "3180a623c9f2c40d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293937,
  "host_pid": "9e6742732c60:1",
  "hash": "b36940b5718cbb0e7b3d03c28a933998f51792c1b705072a848cc9f130410ba7",
  "cid": "QmV1b36940b5718cbb0e7b3d03c28a933998f51792c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293937,
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
      "evaluated_at": 1760293937
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
  "sig": "ee9d75673170e1e135702a3408de294b00bb809760137bde6b81989b0e935017"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1257269292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5514339}}}