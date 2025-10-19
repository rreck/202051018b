```json
{
  "id": "6e77eeb2337b9204",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292902,
  "host_pid": "9e6742732c60:1",
  "hash": "de08a3b096b2c993535a0a26f9e647b5c04e50ddc66398f3308f650a6b3fe6b4",
  "cid": "QmV1de08a3b096b2c993535a0a26f9e647b5c04e50dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292902,
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
      "evaluated_at": 1760292902
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
  "sig": "a7fd8ac7ce154bdb8cc1e37b6daaa5e42849817832043cbb59ed7d7153430cd8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 763245925890246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 93995595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '634500dd7ac761f0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '763245921', 'validation_error': 'Invalid routing number checksum'}}}