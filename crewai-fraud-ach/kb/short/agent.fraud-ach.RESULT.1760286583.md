```json
{
  "id": "edeaa37be7f69a09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286583,
  "host_pid": "9e6742732c60:1",
  "hash": "a47ed0b09c8e688f0e0b5ab824d47f6734f4ff26609407e1c4c23ca6bdda0c70",
  "cid": "QmV1a47ed0b09c8e688f0e0b5ab824d47f6734f4ff26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286583,
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
      "evaluated_at": 1760286583
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "e1c01207d704acc7c097cbe012e4bcbd9af1d500db53b50a831e34fd52858ac8"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 044000031749582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 188281470, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '509963b8d6b047dd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6276049}}}