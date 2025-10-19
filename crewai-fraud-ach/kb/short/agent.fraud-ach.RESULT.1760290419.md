```json
{
  "id": "7be5a30bb459c8db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290419,
  "host_pid": "9e6742732c60:1",
  "hash": "dd746f4fa3af476ede26c139320a9483eb963e2c92e0ac6e412f221d85b72394",
  "cid": "QmV1dd746f4fa3af476ede26c139320a9483eb963e2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290419,
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
      "evaluated_at": 1760290419
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
  "sig": "926bf25f30b7be4c783afd481999dffd3a895677cc3f154435532d61e0b15704"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000028341368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 1281371700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'b11d2debe374bbec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}