```json
{
  "id": "e29981b63be13ab5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292039,
  "host_pid": "9e6742732c60:1",
  "hash": "cd5741cd7391e71bf2513e3a192c1f7bf60c40eab16fc1f37b9e1dfebaeffcb4",
  "cid": "QmV1cd5741cd7391e71bf2513e3a192c1f7bf60c40ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292039,
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
      "evaluated_at": 1760292039
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
  "sig": "1d9a4dc3d6295ee1807162bed373e744aafe8f5335c3ece753a386f28de98213"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 11402370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}maly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.78, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7365830}}}