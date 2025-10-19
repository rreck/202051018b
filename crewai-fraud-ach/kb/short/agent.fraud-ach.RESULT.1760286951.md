```json
{
  "id": "c6b35531b006e8a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286951,
  "host_pid": "9e6742732c60:1",
  "hash": "13585787fc434e43765dfaf0c460238e804e4ce6c115de6d8c74b0b325f9f808",
  "cid": "QmV113585787fc434e43765dfaf0c460238e804e4ce6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286951,
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
      "evaluated_at": 1760286951
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
  "sig": "cc879b9a56e50622694c52d8c6b9b22defcffa14aea088907c47a3d66bd0b66b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594497049
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': 'c5255ffe70702a12'}}}re': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': 'd0d1b4b42d54423e'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7365830}}}