```json
{
  "id": "0c027dfbcebeb579",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292102,
  "host_pid": "9e6742732c60:1",
  "hash": "257e85d54a942301c324e53023f65c53e196929c7af262d1c8d67fa379918663",
  "cid": "QmV1257e85d54a942301c324e53023f65c53e196929c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292102,
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
      "evaluated_at": 1760292102
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
  "sig": "0a42e358305bdd44fedd9fcbdfeec25f8e516b8c2a907f3eb4acedb6f5fd8556"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597475256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 45067620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'c99ab431a9f6998c'}}}