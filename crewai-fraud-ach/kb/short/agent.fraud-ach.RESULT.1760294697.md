```json
{
  "id": "2ff640f03fdf5a90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294697,
  "host_pid": "9e6742732c60:1",
  "hash": "b74d33d722fb7c9f6c14da959607521bc534c96f13c6cbd7751a1e9575bb503c",
  "cid": "QmV1b74d33d722fb7c9f6c14da959607521bc534c96f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294697,
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
      "evaluated_at": 1760294697
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
  "sig": "b915a5450d9e928c72c51ecb0b19ece78e4ea224d5b5cceda9293d856a6e4f18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247483978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 65365785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '670c0389f5bcb489'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018549}}}