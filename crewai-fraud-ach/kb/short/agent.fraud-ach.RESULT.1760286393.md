```json
{
  "id": "31d0d067e2be3eea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286393,
  "host_pid": "9e6742732c60:1",
  "hash": "2b7320ad561770754af8ee9ee4bd6e4c1a484b11dd891b6fc508692699047957",
  "cid": "QmV12b7320ad561770754af8ee9ee4bd6e4c1a484b11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286393,
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
      "evaluated_at": 1760286393
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
  "sig": "9c46e5bbba0143778e0d03af46139f820b2126ac1237b7e6b73412c565b4db17"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 031201463227855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 219471624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': 'a9c92113e6dbf136'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.46, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9144651}}}