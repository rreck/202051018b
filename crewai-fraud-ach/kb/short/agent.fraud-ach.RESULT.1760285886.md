```json
{
  "id": "4624c2d69a517855",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285886,
  "host_pid": "9e6742732c60:1",
  "hash": "e66cfab2d81a0eed8b959b66c5e0bcfed78cf6194eb5412d39ddd841a1d16fa6",
  "cid": "QmV1e66cfab2d81a0eed8b959b66c5e0bcfed78cf619",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285886,
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
      "evaluated_at": 1760285886
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
  "sig": "a3992eed4d84a89813dfc60a4349dcf600a22c42c99ca28249f32b60b0cf93fc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242331672
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}