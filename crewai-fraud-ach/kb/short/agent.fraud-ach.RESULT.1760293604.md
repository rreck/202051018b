```json
{
  "id": "792bbf6b498e22dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293604,
  "host_pid": "9e6742732c60:1",
  "hash": "6cdf2a97e18df16864501b5dca7b9060ca0cab6af39229e1f84ccaf36d95d9a3",
  "cid": "QmV16cdf2a97e18df16864501b5dca7b9060ca0cab6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293604,
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
      "evaluated_at": 1760293604
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
  "sig": "74585b16e891d9850657a480b2f615711068ad37c35d0130a0dcefdd4df3c015"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000028341368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 1896430116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'b11d2debe374bbec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8542478}}}