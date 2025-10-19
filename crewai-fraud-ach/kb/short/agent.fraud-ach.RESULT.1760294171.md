```json
{
  "id": "411a0793c03ef9db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294171,
  "host_pid": "9e6742732c60:1",
  "hash": "2430471df141d435daf99dbe6b540ae81d1785d234b2148d1043986dd1d555a0",
  "cid": "QmV12430471df141d435daf99dbe6b540ae81d1785d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294171,
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
      "evaluated_at": 1760294171
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
  "sig": "e9127c64f04fb891fdf5a9a568753a26b26857ef2c1dd3345e57fb81824a19f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027294403
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 46543614, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}