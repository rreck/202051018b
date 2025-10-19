```json
{
  "id": "94e3e0040360e116",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293990,
  "host_pid": "9e6742732c60:1",
  "hash": "e2d787f4a4d7d7ae1a1fb383c5cc2d9ac0e48add5a689695b8e180e1da36d9a0",
  "cid": "QmV1e2d787f4a4d7d7ae1a1fb383c5cc2d9ac0e48add",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293990,
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
      "evaluated_at": 1760293990
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
  "sig": "7fa4fd880dfa53c10f5cf782abb5c8747765cfd82e0535d8dc3906f844054242"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033181833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 85656305, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '52cd22d87934f676'}}}