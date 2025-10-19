```json
{
  "id": "3113d7795792d076",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292000,
  "host_pid": "9e6742732c60:1",
  "hash": "26e32c68543fbc8c8d33f76416c66f5ad43fbd512ac5303b0e924223a3af01bb",
  "cid": "QmV126e32c68543fbc8c8d33f76416c66f5ad43fbd51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292000,
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
      "evaluated_at": 1760292000
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
  "sig": "ca09e2579a5ecbcc77103f33f2518dba8610af247fbe69ffa32de1fa1e899e07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022330150
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 82844080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'b30e2736c805251a'}}}