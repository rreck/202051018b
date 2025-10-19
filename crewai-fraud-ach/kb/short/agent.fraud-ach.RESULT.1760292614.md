```json
{
  "id": "006166fc57c33e7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292614,
  "host_pid": "9e6742732c60:1",
  "hash": "ed7987b3172f2168c7a4749ac061c05d6c320f4690161c631acb2a4a7390a8da",
  "cid": "QmV1ed7987b3172f2168c7a4749ac061c05d6c320f46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292614,
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
      "evaluated_at": 1760292614
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
  "sig": "09cd7dda570481909a6bff163e3db1cef95093f7dd572e4abf6499249302618e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 47143947, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}