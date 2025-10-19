```json
{
  "id": "c4fbf56995a92260",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293222,
  "host_pid": "9e6742732c60:1",
  "hash": "14707d7afc2bdcb2e41c93e89b37e064a6144ee24276db06f9146a6701963d41",
  "cid": "QmV114707d7afc2bdcb2e41c93e89b37e064a6144ee2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293222,
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
      "evaluated_at": 1760293222
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
  "sig": "629185c01a8095788e004e945d50f6cc5e170d83d19d2d45cbf539976873cecd"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 021000029420003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 1412949980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6602570}}}