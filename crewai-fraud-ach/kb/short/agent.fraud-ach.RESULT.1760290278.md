```json
{
  "id": "fc6bd2d7521d50ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290278,
  "host_pid": "9e6742732c60:1",
  "hash": "a2b46a3115bba48222b262ed94ac94b53c9d0298c97b8e71ef13591d8248435f",
  "cid": "QmV1a2b46a3115bba48222b262ed94ac94b53c9d0298",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290278,
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
      "evaluated_at": 1760290278
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
  "sig": "0e42a627c1bdddb8c1f23db33f7e28f46565917608be98ba17b2ef2897e0f6d9"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000034245036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 1130511288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': '2d29d6825e083497'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}