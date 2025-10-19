```json
{
  "id": "e8aba18ab7dcd0d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286585,
  "host_pid": "9e6742732c60:1",
  "hash": "b1e5cf23867a7922f2704fd9d3613f7ebdce7b0a3d7ab30244d1520351d0e93e",
  "cid": "QmV1b1e5cf23867a7922f2704fd9d3613f7ebdce7b0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286585,
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
      "evaluated_at": 1760286585
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "572d0b8bb660cdbe587535b061c7c5c91025a02ae9ee257239a8063dad100d86"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243177921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10340100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}