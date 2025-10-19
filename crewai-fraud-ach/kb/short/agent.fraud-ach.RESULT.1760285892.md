```json
{
  "id": "7c80c247c1a97adc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285892,
  "host_pid": "9e6742732c60:1",
  "hash": "81ab8718b004e87ba7a12ffb5dc9854fd19bbae09ddcdfe7054efd5688e0f6ad",
  "cid": "QmV181ab8718b004e87ba7a12ffb5dc9854fd19bbae0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285892,
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
      "evaluated_at": 1760285892
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
  "sig": "aaf07498fbdff3518c202e8950e3bed64413f8cb3d17a972cc86cd947f18d76c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469533124
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': '99a5c6f080ea1552'}}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}