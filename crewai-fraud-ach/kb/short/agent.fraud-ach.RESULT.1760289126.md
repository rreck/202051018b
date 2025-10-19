```json
{
  "id": "e170456b923f4483",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289126,
  "host_pid": "9e6742732c60:1",
  "hash": "ce6ba18ea6af9173339cda9409371b8f6f736155b7e0832a9121b43d5aca1765",
  "cid": "QmV1ce6ba18ea6af9173339cda9409371b8f6f736155",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289126,
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
      "evaluated_at": 1760289126
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
  "sig": "a6ec767d3737bf45e9019904f40c627834bb4d735203ff8d4068a1355d4c69f4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 612898027160979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 13462944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '1a410ec770966ef8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}s': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6276049}}}