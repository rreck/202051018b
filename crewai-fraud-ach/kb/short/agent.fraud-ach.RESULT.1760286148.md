```json
{
  "id": "5a290e37a842f7d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286148,
  "host_pid": "9e6742732c60:1",
  "hash": "6a298ed9d5448c2d19a92f029109ddcd3dfe13848e9f801befb7f7fefc425437",
  "cid": "QmV16a298ed9d5448c2d19a92f029109ddcd3dfe1384",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286148,
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
      "evaluated_at": 1760286148
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
  "sig": "edd8265c7ede379601876af12c41fbd01800f4178e5f86333aa4f73c99fcd923"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022959454
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}