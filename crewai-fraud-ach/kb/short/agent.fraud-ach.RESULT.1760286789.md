```json
{
  "id": "4d76d4f680fc4f26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286789,
  "host_pid": "9e6742732c60:1",
  "hash": "58097f2064bbf89422dae5c57a1988c94f55099a1372e39ef4ab43ebb48edd79",
  "cid": "QmV158097f2064bbf89422dae5c57a1988c94f55099a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286789,
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
      "evaluated_at": 1760286789
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
  "sig": "38a1802a231acf50be412fc9598010b06120ae52ae358b1befe75954d126e0bb"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 207374862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5604726}}}