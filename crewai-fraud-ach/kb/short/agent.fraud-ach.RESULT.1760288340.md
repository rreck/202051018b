```json
{
  "id": "0c7fe228ec21ad7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288340,
  "host_pid": "9e6742732c60:1",
  "hash": "d69ac282703b93c298684e1425ae87a5ee547b8757e1b58fb6274406e69afcd9",
  "cid": "QmV1d69ac282703b93c298684e1425ae87a5ee547b87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288340,
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
      "evaluated_at": 1760288340
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
  "sig": "a68e1d976e70ff79bacf3941a25838f375675183a1ac32b215c1c8e4ee9f0f6b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 478694940117269
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 17425800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}