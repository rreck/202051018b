```json
{
  "id": "3b5ddb9c7f93695b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294598,
  "host_pid": "9e6742732c60:1",
  "hash": "8a6d756f65964f38e70226ce1ce133ec42c5e0be18f15b5508d5b9361da1d333",
  "cid": "QmV18a6d756f65964f38e70226ce1ce133ec42c5e0be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294598,
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
      "evaluated_at": 1760294598
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
  "sig": "79c3f2767c46d99d84b3710d016a5ac533fe9cfdf699a77caa4d6cf5a41eff49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597385398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 58882807, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '354842811986f77e'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.17, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8052182}}}