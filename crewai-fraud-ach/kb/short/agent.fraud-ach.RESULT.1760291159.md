```json
{
  "id": "4b3c765ea1ca2345",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291159,
  "host_pid": "9e6742732c60:1",
  "hash": "34943827f2585f1893f37c16cb801306b56bfeb63edd352c0c6decc4489b2fd6",
  "cid": "QmV134943827f2585f1893f37c16cb801306b56bfeb6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291159,
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
      "evaluated_at": 1760291159
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
  "sig": "650878d04d30e8490f831e2ae29479d6d248a644e021fe51a0f265eddef5ed37"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 063100272253110
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 1157770152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': 'c9de6cf87e9b501f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6891489}}}