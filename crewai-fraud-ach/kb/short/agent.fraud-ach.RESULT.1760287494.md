```json
{
  "id": "da0e37d661057bb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287494,
  "host_pid": "9e6742732c60:1",
  "hash": "3c1a9b151c114e2c27df93dddafd978ce17d653c897f86aa48fdef5bfaaf4b79",
  "cid": "QmV13c1a9b151c114e2c27df93dddafd978ce17d653c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287494,
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
      "evaluated_at": 1760287494
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
  "sig": "84b6743bbb664cbc11e2319fb0fe16e3cdc19c0eab670cfca72fc90bd4f84f6f"
}
```

Fraud detected: invalid_routing (score: 84)
Transaction: 039274533993332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 10103706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}