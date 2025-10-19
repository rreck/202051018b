```json
{
  "id": "dbe2fa2b951ec861",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294492,
  "host_pid": "9e6742732c60:1",
  "hash": "c445aa11c0aaa22bb28ffe958c3ebc5c2c3e6776a698b8f9e6a44ac6ec26e6ed",
  "cid": "QmV1c445aa11c0aaa22bb28ffe958c3ebc5c2c3e6776",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294492,
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
      "evaluated_at": 1760294492
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
  "sig": "64784a0c25039036315414cc5453580444699e4241415eadd3fab4e7e82bb3eb"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 1556235355, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6511445}}}