```json
{
  "id": "db3e124d7eeacd20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290271,
  "host_pid": "9e6742732c60:1",
  "hash": "c5353ac69a4bf6c02e0afca907e1617c83ec3d1254c46d1d1f9afc4c10b64c03",
  "cid": "QmV1c5353ac69a4bf6c02e0afca907e1617c83ec3d12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290271,
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
      "evaluated_at": 1760290272
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
  "sig": "bbaa1d3566dc19e007afc097cfb278a6364613cee4f2578b2099c71ed5362312"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 063100277645862
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 950670970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': 'c7c729dc286039c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.3, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6511445}}}