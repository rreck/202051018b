```json
{
  "id": "b141d757d3596fa2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288183,
  "host_pid": "9e6742732c60:1",
  "hash": "802fdb3a36a7d7c3530fbd77a75cbab148a81ea4f7cc872de9721aaccf7977fd",
  "cid": "QmV1802fdb3a36a7d7c3530fbd77a75cbab148a81ea4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288183,
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
      "evaluated_at": 1760288183
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
  "sig": "a331261ee6fb23e515df02827c12737274610abf26092be4e964a9d6681c8d1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 14416935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}