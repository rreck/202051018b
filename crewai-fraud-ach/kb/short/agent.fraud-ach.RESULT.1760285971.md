```json
{
  "id": "f84d846a678606c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285971,
  "host_pid": "9e6742732c60:1",
  "hash": "4eff9052aa76995b49babbbe05a4a99a042574fbc1b518b57d1bf9817c0a449c",
  "cid": "QmV14eff9052aa76995b49babbbe05a4a99a042574fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285971,
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
      "evaluated_at": 1760285971
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
  "sig": "301689836f333790d4d6a56c77151ca28770f1fa818975e73d6c2247675f4a06"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150592686
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}