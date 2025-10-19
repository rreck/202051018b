```json
{
  "id": "c25c9fd871c0fa7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289354,
  "host_pid": "9e6742732c60:1",
  "hash": "ff1f139693c9421a212603432a96d2adf449c71f5c8aadfa831637dd5c0fca87",
  "cid": "QmV1ff1f139693c9421a212603432a96d2adf449c71f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289354,
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
      "evaluated_at": 1760289354
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "50b1d20cc081974a81f75ede5b303268b173c664175c7cb7d0c7d8a2dcfaaeef"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 701651307465811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 25178285, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '31f29b630ea434da'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}