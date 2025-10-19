```json
{
  "id": "6b11ec2b8d025e0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291608,
  "host_pid": "9e6742732c60:1",
  "hash": "daabca0b5e4543cada67ebcae37441062987aad220033078c821737343048854",
  "cid": "QmV1daabca0b5e4543cada67ebcae37441062987aad2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291608,
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
      "evaluated_at": 1760291608
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
  "sig": "68244f95ae1c1e1c3dd837dfdd886a848c5bfb0d6c02ad4ea0e8f45090f8093d"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 122105155084324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 1230692304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}