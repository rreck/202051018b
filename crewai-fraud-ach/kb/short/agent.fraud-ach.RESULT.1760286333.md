```json
{
  "id": "4ddac1e00d0bcee1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286333,
  "host_pid": "9e6742732c60:1",
  "hash": "4511d62a5d2ee268ea090e096f1d903c88171009f0af37881a25c0d02c8c08c4",
  "cid": "QmV14511d62a5d2ee268ea090e096f1d903c88171009",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286333,
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
      "evaluated_at": 1760286333
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
  "sig": "bb337f2411e03ac7ee00ac3beeea3977a0aca538ae7e16e4906ed67c1b8a501e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240263900
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285764, 'matching_hash': 'e5d68d31887f65d4'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}