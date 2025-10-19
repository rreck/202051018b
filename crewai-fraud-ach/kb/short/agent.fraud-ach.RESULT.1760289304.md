```json
{
  "id": "561d8b73cc9bf327",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289304,
  "host_pid": "9e6742732c60:1",
  "hash": "fe10e9ebdb43e54ccfc93ce8377b4224a6f98dc23930ddf5388a9935c3969ad0",
  "cid": "QmV1fe10e9ebdb43e54ccfc93ce8377b4224a6f98dc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289304,
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
      "evaluated_at": 1760289304
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
  "sig": "07905ae94e5079000a1c72853aef59c0db0535e44fd52545a5dd2b559cbe4da6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465632833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 57344196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': '908d3acbf69a371c'}}}