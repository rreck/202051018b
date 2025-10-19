```json
{
  "id": "d1ec5ab7a3cfee5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287214,
  "host_pid": "9e6742732c60:1",
  "hash": "0c9f4552c1a83843d5a44dc8dc49cf94a2941e5e70ccd0df030574b7dc407552",
  "cid": "QmV10c9f4552c1a83843d5a44dc8dc49cf94a2941e5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287214,
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
      "evaluated_at": 1760287214
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
  "sig": "9dcb8d8433f704044ad926423608cc8bbafc3476ec267a9e7a93d0d412870bda"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 20750964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}