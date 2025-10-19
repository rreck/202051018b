```json
{
  "id": "b57039fed0c60cfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288174,
  "host_pid": "9e6742732c60:1",
  "hash": "97a1d89d2b678c24f68d063661faf576287cca921af39d0b644a4f96b6cede9e",
  "cid": "QmV197a1d89d2b678c24f68d063661faf576287cca92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288174,
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
      "evaluated_at": 1760288174
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
  "sig": "5db3fd5a1e5b87f7fa1ac5a45b498f17da0cf3ddba9fc947926f48efd1f41d88"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 063100270473682
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 811546425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': 'dcfb2900505c6ddc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.64, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9547605}}}