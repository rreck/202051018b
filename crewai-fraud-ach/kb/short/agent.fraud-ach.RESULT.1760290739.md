```json
{
  "id": "d36cc42b327c4397",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290739,
  "host_pid": "9e6742732c60:1",
  "hash": "5b9ba06909229d77067b261fb22c3f34915e43d8e5788239bf2af5e8f508af25",
  "cid": "QmV15b9ba06909229d77067b261fb22c3f34915e43d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290739,
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
      "evaluated_at": 1760290739
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
  "sig": "fd2e5d3085019ac4124518ec5765f4adedb9a776bcfcd9fb069561d5ea001ffa"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000246089162
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 1412965876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': '13ee20e814facee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.68, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8942822}}}