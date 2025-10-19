```json
{
  "id": "bbbd5faddc71424b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294667,
  "host_pid": "9e6742732c60:1",
  "hash": "4c7f85f932039d6742de6c6b73da5ff62603639b2683462db6a352d2d453c5d7",
  "cid": "QmV14c7f85f932039d6742de6c6b73da5ff62603639b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294667,
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
      "evaluated_at": 1760294667
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
  "sig": "3a320150d958a9b92151e5e619c9877563acf803a0ad35f6d4bc43e4deaeb56f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 26708572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}maly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.26, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9966572}}}