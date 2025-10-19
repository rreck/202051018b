```json
{
  "id": "5f6799896e6d3c83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286605,
  "host_pid": "9e6742732c60:1",
  "hash": "8352fa90e073813cfdceb245d8a0abccda4431683d6d761071bad726812eea0d",
  "cid": "QmV18352fa90e073813cfdceb245d8a0abccda443168",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286605,
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
      "evaluated_at": 1760286605
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
  "sig": "231e0aeecd100bc19ee2a83fb7aa54647c0f9d966ad77836f5e7b570302bc3fa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023834320
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10943496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285763, 'matching_hash': 'd0d38b811698e46a'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}