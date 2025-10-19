```json
{
  "id": "c13d3265d4e69a74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286680,
  "host_pid": "9e6742732c60:1",
  "hash": "018a347d0200e40fc86393366eaa5a861daab055c55662c80b78f3a86f98b57f",
  "cid": "QmV1018a347d0200e40fc86393366eaa5a861daab055",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286680,
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
      "evaluated_at": 1760286680
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
  "sig": "6390aba8ae774c4349fe052825c399ef63d4062e9cc2c3f1a50abf4f771bf95f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022308418
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': 'f2b6499d63eb1b6e'}}}