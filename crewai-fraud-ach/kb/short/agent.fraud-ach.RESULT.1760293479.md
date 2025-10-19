```json
{
  "id": "04289607ad1508c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293479,
  "host_pid": "9e6742732c60:1",
  "hash": "df43105f684b253cfdf2d61c6ea9b449f11ff403c5fdefcd86091641d27422a2",
  "cid": "QmV1df43105f684b253cfdf2d61c6ea9b449f11ff403",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293479,
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
      "evaluated_at": 1760293479
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
  "sig": "4c41d7ec7ff4ac5aba8ff2fedc7835962c182b07e4e0468bc56a6a209815b442"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029313979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 103505313, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': 'ee97e2abac1557d2'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}