```json
{
  "id": "81b9933e766f130e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290319,
  "host_pid": "9e6742732c60:1",
  "hash": "ae8035ada23906f8d36f4ad62ab2dec28e06ec918b09fd6a3621c9542149ae35",
  "cid": "QmV1ae8035ada23906f8d36f4ad62ab2dec28e06ec91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290319,
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
      "evaluated_at": 1760290319
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
  "sig": "5b5cd147a6950c80c244c83d9d58afa2581067754de25ba322ce8d2ab7bc9e69"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 1256744748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8549284}}}