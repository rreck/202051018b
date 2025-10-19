```json
{
  "id": "fcbbf6ac5aeb3ba5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293485,
  "host_pid": "9e6742732c60:1",
  "hash": "d1ee53974c2925b7e140017750364852d3ed5b8f5fd33dfe96bd7ac5832afd65",
  "cid": "QmV1d1ee53974c2925b7e140017750364852d3ed5b8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293485,
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
      "evaluated_at": 1760293485
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
  "sig": "e09e8a3e178f556e697924e86f80ff6227599b26321710dd602eb30d5a477d59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 10950000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}