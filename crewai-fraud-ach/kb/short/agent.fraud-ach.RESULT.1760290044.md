```json
{
  "id": "9444add0cfd9bb63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290044,
  "host_pid": "9e6742732c60:1",
  "hash": "d200bd79a3d35d36508eb445ed764b8c2a1eac81e58bdb0bf1376cb7167db32b",
  "cid": "QmV1d200bd79a3d35d36508eb445ed764b8c2a1eac81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290044,
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
      "evaluated_at": 1760290044
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
  "sig": "8b6bb4b5a915d2104402da5419cc9a372f097fe5681bd0f68fa5c4dd64d933c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712325
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 50939140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '06a9425dc3ac5c5b'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8052182}}}