```json
{
  "id": "422fab0b1be1ab0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294442,
  "host_pid": "9e6742732c60:1",
  "hash": "c6cf909add3c4f9dfd2a96ae25f83612d836e7a3373261361495924eea8d198e",
  "cid": "QmV1c6cf909add3c4f9dfd2a96ae25f83612d836e7a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294442,
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
      "evaluated_at": 1760294442
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
  "sig": "b6204564c91651687e77a4136edab1e63515ee98c6cd5c2e64d22c978ef2ab10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247109361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 22527414, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '3efad933d2b7f9bd'}}}maly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6892469}}}