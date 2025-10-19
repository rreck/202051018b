```json
{
  "id": "31c6963b6a136f9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286427,
  "host_pid": "9e6742732c60:1",
  "hash": "6865c2cb3a38df2882f4139979161f0131f2cf75bc8a0ab4a2c218c6bd9f0207",
  "cid": "QmV16865c2cb3a38df2882f4139979161f0131f2cf75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286427,
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
      "evaluated_at": 1760286427
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "74789262a2bb9c64220395cc8fa47b5524bc1ff9b68c1cc78462d31ef14ef9cc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11225650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8018325}}}