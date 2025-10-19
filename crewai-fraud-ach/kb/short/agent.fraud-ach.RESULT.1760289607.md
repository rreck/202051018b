```json
{
  "id": "cf717ab687e4b20c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289607,
  "host_pid": "9e6742732c60:1",
  "hash": "970ea1a045c4500f4d9d75c5d7902f43f3c7141254a2af9620a564846f476cc1",
  "cid": "QmV1970ea1a045c4500f4d9d75c5d7902f43f3c71412",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289607,
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
      "evaluated_at": 1760289607
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
  "sig": "6ecd995388704f6066c8a2c38f742feb417232ed6c36459be95ad91f3acee25e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 503193792297075
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 53527552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}