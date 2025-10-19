```json
{
  "id": "f02a89dc4242f5c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294060,
  "host_pid": "9e6742732c60:1",
  "hash": "d3dde1ac3d04d69841b0ea73b19c425c46ff6db93973320a69a3388153b3699f",
  "cid": "QmV1d3dde1ac3d04d69841b0ea73b19c425c46ff6db9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294060,
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
      "evaluated_at": 1760294060
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
  "sig": "a0ab385455c3cc8a1c89fdd36a7e5b90043126c95c9f0b1dbc34449059627547"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247483978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 62137845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '670c0389f5bcb489'}}}