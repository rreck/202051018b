```json
{
  "id": "ceb46778708eb3dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294134,
  "host_pid": "9e6742732c60:1",
  "hash": "91e2dc6d388798f80d8fcad6334f5a4bd69d98aa0898f3d21bbee0bd0e3f2761",
  "cid": "QmV191e2dc6d388798f80d8fcad6334f5a4bd69d98aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294134,
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
      "evaluated_at": 1760294134
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
  "sig": "0f3dd1f6771c5097172895b78f86e738b65937adfa3dab0655ccc4f304bb9dc4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599908299
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 102378352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '494601c315920761'}}}aly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7743228}}}