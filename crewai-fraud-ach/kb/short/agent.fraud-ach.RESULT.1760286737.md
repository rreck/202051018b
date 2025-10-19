```json
{
  "id": "6f507a9ac9fd248b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286737,
  "host_pid": "9e6742732c60:1",
  "hash": "ddc80dc5a601c515570f310d4d05d1d6b5e1277bc8ce81e5dc65001e27f347c5",
  "cid": "QmV1ddc80dc5a601c515570f310d4d05d1d6b5e1277b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286737,
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
      "evaluated_at": 1760286737
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
  "sig": "9b3f0aca1ecb7fabd23a16af065cb346d7cf190b2b42f04a7d0d5b35d4bcf956"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153539871
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '6120bfc166994b37'}}}