```json
{
  "id": "f56d0264aedfb5eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288826,
  "host_pid": "9e6742732c60:1",
  "hash": "12a970cb8dd8a0c79f43c20a4c0f0fa8e5ba523e4e7030e2d11d750c7a3d3c0f",
  "cid": "QmV112a970cb8dd8a0c79f43c20a4c0f0fa8e5ba523e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288826,
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
      "evaluated_at": 1760288826
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
  "sig": "ba80b1b66ecd530e6a4f0210d72e67ebf67de5a0f51cbb0f9b9fd0f4dc2696bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240751710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': 'c9609c1b2bce9c12'}}}765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8549284}}}