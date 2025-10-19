```json
{
  "id": "4546020e22e21211",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294278,
  "host_pid": "9e6742732c60:1",
  "hash": "8299568da1917c8ca0993aea3b18688531ca178445c4a4c5aa40d198857cc081",
  "cid": "QmV18299568da1917c8ca0993aea3b18688531ca1784",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294278,
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
      "evaluated_at": 1760294278
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
  "sig": "f01002383ca3012f93a0bb6264dbc9f1f620875f2179cf4f31d82d9bf8f45452"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025362322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 82399225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '755a8d21dcb7f46a'}}}maly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.49, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6849877}}}