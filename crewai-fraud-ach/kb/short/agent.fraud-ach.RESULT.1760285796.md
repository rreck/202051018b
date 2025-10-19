```json
{
  "id": "d110f02fa577345a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285796,
  "host_pid": "9e6742732c60:1",
  "hash": "c6da7ad4510e758c129e0fa1d6f3cbfd81f2fa6d567a334b932b17632cdcfd3c",
  "cid": "QmV1c6da7ad4510e758c129e0fa1d6f3cbfd81f2fa6d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285796,
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
      "evaluated_at": 1760285796
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
  "sig": "d4e4e9e58dca29c921c10c9b172c10eb7e32161b809658a0be5f1aeaf27cd4a0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037990803
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}