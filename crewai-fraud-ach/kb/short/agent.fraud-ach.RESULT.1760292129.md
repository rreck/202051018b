```json
{
  "id": "da31855e3c88f81c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292129,
  "host_pid": "9e6742732c60:1",
  "hash": "48bf56578796d9cfe8ef94ba8b7f3f18b511a934b88366390e38e3cae62b9e81",
  "cid": "QmV148bf56578796d9cfe8ef94ba8b7f3f18b511a934",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292129,
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
      "evaluated_at": 1760292129
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
  "sig": "b394ce6a15cccacdb0f07e500434301193545611814fb788b337ea89b0e63961"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241272290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 32917704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'ac7868cb6249fe41'}}}