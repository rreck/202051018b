```json
{
  "id": "d70a2d2756dd98b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292643,
  "host_pid": "9e6742732c60:1",
  "hash": "f80e8b9aa78e46c558f91307f3671f95aaf6772a5986a7c1ebe97d3a9b0c5cda",
  "cid": "QmV1f80e8b9aa78e46c558f91307f3671f95aaf6772a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292643,
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
      "evaluated_at": 1760292643
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
  "sig": "1e39861f93167d49a60d7cc629d1406ec3a6da51add922977d56fde146d93b33"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 1315311890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6511445}}}