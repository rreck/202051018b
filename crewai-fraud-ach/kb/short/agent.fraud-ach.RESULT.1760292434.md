```json
{
  "id": "9a0503ac45c0d1c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292434,
  "host_pid": "9e6742732c60:1",
  "hash": "79200cd69977374ddef51720daa095ccd328003eb140131b188efb21a8fda2e4",
  "cid": "QmV179200cd69977374ddef51720daa095ccd328003e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292434,
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
      "evaluated_at": 1760292434
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
  "sig": "dae05d8f521f5d0b35fa091be471f9da8a269ea1ab374f0389e0da80c68f2191"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 95488461, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}