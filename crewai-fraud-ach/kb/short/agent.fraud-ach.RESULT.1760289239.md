```json
{
  "id": "3e22ae268b669cf9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289239,
  "host_pid": "9e6742732c60:1",
  "hash": "6feacb10ba7bd06e234410eec8b761b20bbffdb1bfcaf580a2b909e778fb6389",
  "cid": "QmV16feacb10ba7bd06e234410eec8b761b20bbffdb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289239,
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
      "evaluated_at": 1760289239
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
  "sig": "b2e5d0fb238d7dd5552933bf7be4ad86b22e85a8e26e8b7f9de19a7fe47f49d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 31657158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}