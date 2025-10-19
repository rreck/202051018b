```json
{
  "id": "4da89ad736501a2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292280,
  "host_pid": "9e6742732c60:1",
  "hash": "622895caee64065616969fe5c8ceed4d580ac0fe574499bc4c5a0958c46b981b",
  "cid": "QmV1622895caee64065616969fe5c8ceed4d580ac0fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292280,
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
      "evaluated_at": 1760292280
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
  "sig": "8b87693c6781c68f0d86a1dbba98e139bff277a103abc0a980eba94d4bfa5cb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 52077166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}