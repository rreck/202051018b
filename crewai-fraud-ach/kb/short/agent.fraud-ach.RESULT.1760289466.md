```json
{
  "id": "09df3d384124478a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289466,
  "host_pid": "9e6742732c60:1",
  "hash": "151117cb0fc009c323f4d521aaade3b3e28143d7e7f9d0da398a136ed187ede9",
  "cid": "QmV1151117cb0fc009c323f4d521aaade3b3e28143d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289466,
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
      "evaluated_at": 1760289466
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
  "sig": "9c6edc824d5ed6895796c434029c815e37f9bfb17872ab066b7044de33f0e0bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245084656
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 43277488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '11924a0da29b01ce'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}