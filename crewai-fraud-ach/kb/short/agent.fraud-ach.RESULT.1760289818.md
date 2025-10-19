```json
{
  "id": "f8166c78c7b8dc58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289818,
  "host_pid": "9e6742732c60:1",
  "hash": "62c723d519771ebf59d653a12ec15e7b014c91c0cb773d9d7c12b7e1e647db91",
  "cid": "QmV162c723d519771ebf59d653a12ec15e7b014c91c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289818,
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
      "evaluated_at": 1760289818
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
  "sig": "8b79446d86ab68d54552a490bd18d815e5ef2dbdc7fe71c30c18e59f389ba903"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 031201463227855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 1225383234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'a9c92113e6dbf136'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9144651}}}