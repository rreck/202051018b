```json
{
  "id": "48bfd1e9357036ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286473,
  "host_pid": "9e6742732c60:1",
  "hash": "404aa7ab7ccd089082752db182db4c113a6d8cca35ddd737dcd6628dd3ca3554",
  "cid": "QmV1404aa7ab7ccd089082752db182db4c113a6d8cca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286473,
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
      "evaluated_at": 1760286473
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
  "sig": "9b7941192f9f27385b98c1be7ab6af7d6a9b6031cd37fd5796dbd878dbe37a47"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243232456
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '1b0a7dc1f650d378'}}}