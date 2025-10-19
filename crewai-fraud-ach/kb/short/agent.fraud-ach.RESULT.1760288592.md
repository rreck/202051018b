```json
{
  "id": "e58d64d82a56f522",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288592,
  "host_pid": "9e6742732c60:1",
  "hash": "cb6a68cb2b4a10c1b9369567b7398adb19aacb231eece62a990612a0d7c113b4",
  "cid": "QmV1cb6a68cb2b4a10c1b9369567b7398adb19aacb23",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288592,
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
      "evaluated_at": 1760288592
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
  "sig": "397d0040e82fa32e39bcf5874d87e0f343c900ac9ac2e4dc7e4e3231194ae5a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276282888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 37427964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '2c6b6a2c3736dbce'}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6178432}}}