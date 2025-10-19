```json
{
  "id": "2c338f307d2d0735",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293340,
  "host_pid": "9e6742732c60:1",
  "hash": "9f0cb129c3fb9fe8a6b508ed4e4306e851f8d02ce4c8e86045e919ff262b09c8",
  "cid": "QmV19f0cb129c3fb9fe8a6b508ed4e4306e851f8d02c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293340,
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
      "evaluated_at": 1760293340
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
  "sig": "0cbfd90f0c2d5a0407b8bcac28a14c7edfb007ecff4642b78e9843778d9257ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 83909520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}