```json
{
  "id": "5fd6b837df958361",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291650,
  "host_pid": "9e6742732c60:1",
  "hash": "22c4dc9d85e6ee2a8069649f74285e027f20c73087a15f8912056de7ad282ff5",
  "cid": "QmV122c4dc9d85e6ee2a8069649f74285e027f20c730",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291650,
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
      "evaluated_at": 1760291650
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
  "sig": "710d9249805c52cb05b0ebb47c0c13a43844d9e5dc85d23a2951978d617b0d1a"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270720281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 1662697980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9237211}}}