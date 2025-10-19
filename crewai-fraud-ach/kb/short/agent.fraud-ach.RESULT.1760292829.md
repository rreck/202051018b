```json
{
  "id": "e1ce645dd5c58c5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292829,
  "host_pid": "9e6742732c60:1",
  "hash": "4588ec3e5daa1fd2719293bdfdad006f00565b022f5e4f5abb5dc139daf9566c",
  "cid": "QmV14588ec3e5daa1fd2719293bdfdad006f00565b02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292829,
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
      "evaluated_at": 1760292829
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
  "sig": "f200c9b6fe11b36badb3ce6d002fc86c02112cdf637479b8fb13d3ebbad73e2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032979175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 67481068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '92afbef802abc12c'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9237211}}}