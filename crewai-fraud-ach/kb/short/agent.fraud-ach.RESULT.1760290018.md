```json
{
  "id": "a42a1b7e48cc8bbc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290018,
  "host_pid": "9e6742732c60:1",
  "hash": "d99e6e26fba40bdee74af4c88c78fbd25741022d73c8a3c9a0ae20ebc4ad9ee2",
  "cid": "QmV1d99e6e26fba40bdee74af4c88c78fbd25741022d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290018,
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
      "evaluated_at": 1760290018
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
  "sig": "88c795d3780d40a404f8412d706b73e8d16d61140074204211393237b4dee354"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 58876091, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}