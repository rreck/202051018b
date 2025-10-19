```json
{
  "id": "c00aca2396909b0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290934,
  "host_pid": "9e6742732c60:1",
  "hash": "e68536443b592030a4fa8d4f6e10e2855671ab9d60df2d1ea6949b1599d83aa1",
  "cid": "QmV1e68536443b592030a4fa8d4f6e10e2855671ab9d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290934,
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
      "evaluated_at": 1760290934
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1b167f32a49b5d0e6c94fc8200ce942712163f548c057ff3c7343c84a43cdf86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024343993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 47088418, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '423e45fba5759e5c'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}