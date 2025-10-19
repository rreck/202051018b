```json
{
  "id": "23625fbf3dc63972",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286056,
  "host_pid": "9e6742732c60:1",
  "hash": "b54bfa7ce5cb151b07f143f4513990864d0f839a59df40f71cdfa43fce215061",
  "cid": "QmV1b54bfa7ce5cb151b07f143f4513990864d0f839a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286056,
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
      "evaluated_at": 1760286056
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
  "sig": "575d60c6a7f08276cf50f8fbd6cd93df5218e7e4d37f1f101d3b2fe2b7b01c8f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000035823466
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}