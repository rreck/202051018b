```json
{
  "id": "fb5b5b64bd16fc5a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290674,
  "host_pid": "9e6742732c60:1",
  "hash": "ae6a9c8643e54bb9408dee7035c7eee3709d28535c05ef75bffdf4e420107095",
  "cid": "QmV1ae6a9c8643e54bb9408dee7035c7eee3709d2853",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290674,
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
      "evaluated_at": 1760290674
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
  "sig": "b8ca0c27479935ddfc5d9aeb6fc683340cbade0a43c9bf3849c29ce35edcf81a"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 111000028335360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 1160173872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285764, 'matching_hash': '8e80efed4b38ef8e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.82, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7437012}}}