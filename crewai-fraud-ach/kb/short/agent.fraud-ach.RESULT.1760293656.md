```json
{
  "id": "1b684ff9e3571f8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293656,
  "host_pid": "9e6742732c60:1",
  "hash": "fd59074ec6d4473fc17192e0c4b690189a0f73b6aa2568836fb2581fefec4df0",
  "cid": "QmV1fd59074ec6d4473fc17192e0c4b690189a0f73b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293656,
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
      "evaluated_at": 1760293656
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
  "sig": "6212da7f7a0dd1fff1c4ea79822a864eef6e0b83bcb3bcefe57e984528c4fee9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 24515282, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}maly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6161479}}}