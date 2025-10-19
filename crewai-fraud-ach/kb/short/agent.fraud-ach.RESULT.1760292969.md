```json
{
  "id": "e6e5dc52fa793f53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292969,
  "host_pid": "9e6742732c60:1",
  "hash": "70a02ade3e0c0e33f9e58e7648b563825d9d8bc3e41fae23c3a43bb23c3aaef9",
  "cid": "QmV170a02ade3e0c0e33f9e58e7648b563825d9d8bc3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292969,
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
      "evaluated_at": 1760292969
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
  "sig": "fdf0f44ffa910469c35f652907daba03b85b638f8bb324ef84c4c6f3985fe9c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 66618750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018549}}}