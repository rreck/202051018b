```json
{
  "id": "afb12fcc2630f76c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292661,
  "host_pid": "9e6742732c60:1",
  "hash": "447933aa805d7d2e232d86ee2a5324eb1b432576952c1cd547c28af00d298cc3",
  "cid": "QmV1447933aa805d7d2e232d86ee2a5324eb1b432576",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292661,
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
      "evaluated_at": 1760292661
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
  "sig": "6d190667d2385b87167a3b42a905e85719951964ad911c917eb7b4b9d184b878"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 47378494, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}