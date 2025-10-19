```json
{
  "id": "e1655a92e4a7eea9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285885,
  "host_pid": "9e6742732c60:1",
  "hash": "ed4e1992c1755168271fd62b5ba10bd4d988c9ab8889b6bef367f3bc76003b0a",
  "cid": "QmV1ed4e1992c1755168271fd62b5ba10bd4d988c9ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285885,
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
      "evaluated_at": 1760285885
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
  "sig": "b2f8b0cebc93d9888e6165b9e0c9af95ebe52046edb9133587af16b24af6b88d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242269046
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': '94969c5585cd0fc1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}