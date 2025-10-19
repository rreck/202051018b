```json
{
  "id": "b9701e1657afac39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289445,
  "host_pid": "9e6742732c60:1",
  "hash": "08d27a96bb19d71298925fb1d78f4ed55e1049207f13c41dbe2e750f91be4d29",
  "cid": "QmV108d27a96bb19d71298925fb1d78f4ed55e104920",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289445,
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
      "evaluated_at": 1760289445
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
  "sig": "519769c8ed46b36b4111da894cf93e0e4cdb6db541b991bc5860276e9ee6a589"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 044000032002639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 977705475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '27a8182d1a86d123'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7948825}}}