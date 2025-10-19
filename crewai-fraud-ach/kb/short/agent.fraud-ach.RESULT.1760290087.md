```json
{
  "id": "e618955d3cda2aaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290087,
  "host_pid": "9e6742732c60:1",
  "hash": "3312a9582c25182689614f662e352afde296f2b024c9f83973aa98e401ed5566",
  "cid": "QmV13312a9582c25182689614f662e352afde296f2b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290087,
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
      "evaluated_at": 1760290087
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
  "sig": "d001b77003e7120d81e335ec811b3e2e0ba2a6a86e9663741c2e5d3852064618"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 50998431, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}