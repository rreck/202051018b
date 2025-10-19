```json
{
  "id": "fe2fd0d2aab30afe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294548,
  "host_pid": "9e6742732c60:1",
  "hash": "d1642f007c85bc575e50f17bc5eeb46b111c91f829c26ae0781e41560c3485a3",
  "cid": "QmV1d1642f007c85bc575e50f17bc5eeb46b111c91f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294548,
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
      "evaluated_at": 1760294548
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
  "sig": "0d94e8e281541e3f7d3dd48d823c1aee04ce219c2917a11954e978c3d30493ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150592686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 15124560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8595712}}}