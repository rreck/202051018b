```json
{
  "id": "b8dd2a672805b75b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292971,
  "host_pid": "9e6742732c60:1",
  "hash": "9906e7a64cf6790fe2d5645ad044e61c0e3c52fb4732d577249522f82e587389",
  "cid": "QmV19906e7a64cf6790fe2d5645ad044e61c0e3c52fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292971,
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
      "evaluated_at": 1760292971
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
  "sig": "061ea912750fe6399f18a66dfa228766738a88cbc4d3fbd99025db4ab212e279"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599855850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 75573146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}maly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9947388}}}