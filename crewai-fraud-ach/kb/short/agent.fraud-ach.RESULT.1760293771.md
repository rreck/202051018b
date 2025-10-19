```json
{
  "id": "0ca43968fd5b86e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293771,
  "host_pid": "9e6742732c60:1",
  "hash": "85b2deea2864d2f728274c44546ae4e1d5ac237dd3c5bebf8f836fa6bb77643a",
  "cid": "QmV185b2deea2864d2f728274c44546ae4e1d5ac237d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293771,
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
      "evaluated_at": 1760293771
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
  "sig": "c1529387adcd3f9056afd9728196f4dffe8709d5d63ac567a8303072b1f5e0eb"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000034245036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 1742226300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '2d29d6825e083497'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7743228}}}