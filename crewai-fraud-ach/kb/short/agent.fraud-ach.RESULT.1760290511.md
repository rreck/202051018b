```json
{
  "id": "59b78dc12432f282",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290511,
  "host_pid": "9e6742732c60:1",
  "hash": "256bceb12a9c95602bab86be705c572d4a342185c018fdab5edac292f2e0663d",
  "cid": "QmV1256bceb12a9c95602bab86be705c572d4a342185",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290511,
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
      "evaluated_at": 1760290511
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
  "sig": "38a49b89c5d80d3760a574bf2bd6d90602f4802ee6bc462478f9966c3012a92c"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 044000031749582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 953959448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '509963b8d6b047dd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6276049}}}