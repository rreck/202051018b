```json
{
  "id": "3313b2b2003d303b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290895,
  "host_pid": "9e6742732c60:1",
  "hash": "2150c4d128eda1749059bb9977c90019ae2ceee12fd6d5d49e556bc6dce11696",
  "cid": "QmV12150c4d128eda1749059bb9977c90019ae2ceee1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290895,
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
      "evaluated_at": 1760290895
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
  "sig": "f65ac41ddebde324d9d0a3577d6c3e8b221beb2d1b6f7c1fb6b571ef600e06fa"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100270720281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 1496428182, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9237211}}}