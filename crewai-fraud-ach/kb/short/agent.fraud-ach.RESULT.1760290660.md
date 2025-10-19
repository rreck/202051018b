```json
{
  "id": "4b0b8a59b1a5c633",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290660,
  "host_pid": "9e6742732c60:1",
  "hash": "da4ee6aaff4a06557ef469c528047548398355b4bd3832ffd4c7940797498bfa",
  "cid": "QmV1da4ee6aaff4a06557ef469c528047548398355b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290660,
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
      "evaluated_at": 1760290660
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
  "sig": "1fa0624d95c0029403565f66a91a16ca23fb790b8ea1dca89c23a6ee8cd3a7c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 70933668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8595712}}}