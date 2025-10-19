```json
{
  "id": "8b11a7e006780701",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286302,
  "host_pid": "9e6742732c60:1",
  "hash": "4c269f590ea446c42edf8b47fd4b44c92afea923d1a32c17135a3fbe2ec445c5",
  "cid": "QmV14c269f590ea446c42edf8b47fd4b44c92afea923",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286302,
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
      "evaluated_at": 1760286302
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
  "sig": "108fdedc9edb298c5609b47ecacfa07bbe1857dc5d71daccdb65ff8a096c539c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463230515
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': '5ad257fb4ff4bc47'}}}re': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285764, 'matching_hash': '73d2316250f00dec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8052182}}}