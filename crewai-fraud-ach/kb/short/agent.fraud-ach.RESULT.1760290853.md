```json
{
  "id": "3557160377ea9087",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290853,
  "host_pid": "9e6742732c60:1",
  "hash": "6f0f126e9bf548731471cf25dccdd01236c13930b9bf8e4d1d4cf56a9154cfae",
  "cid": "QmV16f0f126e9bf548731471cf25dccdd01236c13930",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290853,
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
      "evaluated_at": 1760290853
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
  "sig": "e6be82f314d375bfd2692914626428c7407f4de060435ed1d5ee071c81f5ea63"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029133644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 78328754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': 'fa9b9676ccddb30b'}}}