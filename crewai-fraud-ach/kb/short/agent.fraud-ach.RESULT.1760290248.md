```json
{
  "id": "d09cc52baebb1c45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290248,
  "host_pid": "9e6742732c60:1",
  "hash": "c8e65f733cb912899d6518ac408d5f28760562d82c8f75d85b08dcfd81d1fffc",
  "cid": "QmV1c8e65f733cb912899d6518ac408d5f28760562d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290248,
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
      "evaluated_at": 1760290248
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
  "sig": "c14f5a0d3e7cc6eac80404dbae3bda9cb44f0374dc65e2f2b6d5ded1fdf1bbf2"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000242247066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 1317580200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': '1251c161514af894'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.76, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9086760}}}