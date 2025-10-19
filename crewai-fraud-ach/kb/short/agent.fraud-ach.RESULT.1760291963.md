```json
{
  "id": "bbf7ee7bd889b561",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291963,
  "host_pid": "9e6742732c60:1",
  "hash": "1059a7918e6ae4872df40d00d2ea120cc2553dd7a0ed008ddea90ff2db9be36c",
  "cid": "QmV11059a7918e6ae4872df40d00d2ea120cc2553dd7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291963,
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
      "evaluated_at": 1760291963
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
  "sig": "fdeaaf4afa8c4132bd38f06c5283c7d9ada55fd577b6f82ec16c7acb743a785b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277234112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 70500496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': '11106d4d9e5d055e'}}}maly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6178432}}}