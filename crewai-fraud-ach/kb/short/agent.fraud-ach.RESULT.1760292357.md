```json
{
  "id": "44421a6782d88130",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292357,
  "host_pid": "9e6742732c60:1",
  "hash": "dec851f2c7187353a5c916d32dc46f55c09a6c9111999e202d5a681dba210eec",
  "cid": "QmV1dec851f2c7187353a5c916d32dc46f55c09a6c91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292357,
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
      "evaluated_at": 1760292357
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
  "sig": "36e1df941f18e057dbefaac9a07490e202100b7be76c7eb6ece1ec255087d6dd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270864889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 37261364, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'c03eacc7eaf45e0d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}