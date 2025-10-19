```json
{
  "id": "f8e9a423350a4721",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288466,
  "host_pid": "9e6742732c60:1",
  "hash": "ab95882e86cda08fa12c58dc4f5352850c5f0d4f4afb2b28b03cbba82a264747",
  "cid": "QmV1ab95882e86cda08fa12c58dc4f5352850c5f0d4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288466,
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
      "evaluated_at": 1760288466
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
  "sig": "62eb4341fd3588b5a83d5c9545b654ac1a371295caba898330f197403a9efdd0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 033505362547520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 22325846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}