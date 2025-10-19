```json
{
  "id": "c55dac1bc4801081",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289496,
  "host_pid": "9e6742732c60:1",
  "hash": "e3d8e365989c219208ae76e36cde555ee73873b1683413f4eebafe9281a77886",
  "cid": "QmV1e3d8e365989c219208ae76e36cde555ee73873b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289496,
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
      "evaluated_at": 1760289496
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
  "sig": "9a83e37ce4f756e31647413941c493d33860165b7e0fbdd476b811a6776c3424"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022025451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 58555625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}