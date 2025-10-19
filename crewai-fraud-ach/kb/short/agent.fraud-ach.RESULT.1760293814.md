```json
{
  "id": "174c899ee178b356",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293814,
  "host_pid": "9e6742732c60:1",
  "hash": "03b1d0beb93ca4c08906ce99d7f85bc35bb45baf94f0fb15180626357f1b6e0a",
  "cid": "QmV103b1d0beb93ca4c08906ce99d7f85bc35bb45baf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293814,
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
      "evaluated_at": 1760293814
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
  "sig": "afb75c6a9d0ff19d6fd1004d397771ea6e70a5de181fbfab4935169cc390627d"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100275656907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 1557697994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '3d5aab5dd753a251'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6892469}}}