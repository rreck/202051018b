```json
{
  "id": "6be55932bd292b48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288305,
  "host_pid": "9e6742732c60:1",
  "hash": "f491d9ecaab1e6e63366ced2e05edf2459106fe646492aac7bb209448652fd96",
  "cid": "QmV1f491d9ecaab1e6e63366ced2e05edf2459106fe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288305,
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
      "evaluated_at": 1760288305
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
  "sig": "d7473baacbeade2c760d63931ceb12ec308e292c64be4b298061b3286ff4c626"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 676666911893287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 34706262, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '67218afda9e45d8d'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}