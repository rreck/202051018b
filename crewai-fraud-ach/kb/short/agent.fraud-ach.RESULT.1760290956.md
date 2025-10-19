```json
{
  "id": "fcc64001e12eb766",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290956,
  "host_pid": "9e6742732c60:1",
  "hash": "212c62b88bcf9748d782fd2701ff19b294b3213d7809574af3ce9bb6ef31e1fb",
  "cid": "QmV1212c62b88bcf9748d782fd2701ff19b294b3213d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290956,
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
      "evaluated_at": 1760290956
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
  "sig": "cf6dd667f563ffc1502d9bbf71a3076a74f2ba3a0ed9cc72db353f640711beb1"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 026009598348562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 1366282626, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '08c1aa7df797b6df'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.36, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8382102}}}