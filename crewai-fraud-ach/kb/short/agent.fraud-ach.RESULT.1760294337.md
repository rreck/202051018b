```json
{
  "id": "010fa1bcaff4c0f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294337,
  "host_pid": "9e6742732c60:1",
  "hash": "e0fb2b29e265032e3d91889c6af601044dd2afc675945ae42a1f37f88f1d4037",
  "cid": "QmV1e0fb2b29e265032e3d91889c6af601044dd2afc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294337,
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
      "evaluated_at": 1760294337
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
  "sig": "273fbe3406007a09f68d5870eb6d0e4e402ef5c2453190f162fc3409afbcf16b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 43339984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}maly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6178432}}}