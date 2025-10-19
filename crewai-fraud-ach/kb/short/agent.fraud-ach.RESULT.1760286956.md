```json
{
  "id": "b4496d0ec8624988",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286956,
  "host_pid": "9e6742732c60:1",
  "hash": "50f7c6e30787329613740f7b2b3687214d08f88437dfb8d8475ea3060b4f5133",
  "cid": "QmV150f7c6e30787329613740f7b2b3687214d08f884",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286956,
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
      "evaluated_at": 1760286956
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
  "sig": "0e9ce4e5aa60f665a1d713a94d485703efdfe0c13b035e25dfbba15217e2a0b7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591361030
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': '0549fb1f2e5dea5b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}