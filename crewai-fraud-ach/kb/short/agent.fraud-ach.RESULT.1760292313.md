```json
{
  "id": "26a593e06135c91a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292313,
  "host_pid": "9e6742732c60:1",
  "hash": "b19d01b70ba78c9372bfafbffe1b7c3cd5fc7a5c95b772680ee48717f7c05a87",
  "cid": "QmV1b19d01b70ba78c9372bfafbffe1b7c3cd5fc7a5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292313,
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
      "evaluated_at": 1760292313
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
  "sig": "e15b12944532d67888a966836bcda9e8e375be0f3886539bb65cd28f66ae49cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 21343140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}