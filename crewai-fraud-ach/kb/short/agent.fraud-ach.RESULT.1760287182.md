```json
{
  "id": "87fb0ee91337115f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287182,
  "host_pid": "9e6742732c60:1",
  "hash": "5cf55a2a4c950bf8088ef78bc3b1ac9db6bb56e44b3e6cb12dc9ddaff8168e58",
  "cid": "QmV15cf55a2a4c950bf8088ef78bc3b1ac9db6bb56e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287182,
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
      "evaluated_at": 1760287182
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "296302f66ae19d0c740b31e80b59bfc9847e99254af0f72ee9d12ae9dd12864d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000022136987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 18136824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': 'e25bac2e01df376b'}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.14, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8435125}}}