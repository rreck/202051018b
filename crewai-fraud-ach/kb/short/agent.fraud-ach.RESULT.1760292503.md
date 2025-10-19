```json
{
  "id": "72d303fae25e81e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292503,
  "host_pid": "9e6742732c60:1",
  "hash": "2a8915c7b094ddaa0d3ecf8f458bec7190dea64eabeb9920d5f74637fd6698af",
  "cid": "QmV12a8915c7b094ddaa0d3ecf8f458bec7190dea64e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292503,
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
      "evaluated_at": 1760292503
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
  "sig": "0c0e9904c6136254d5680a392de575fecd68a63f2846cd8ee418e6a5141b9de2"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 044000032483239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 1839820869, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': '7bd2e976d6ef9e3c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9245331}}}