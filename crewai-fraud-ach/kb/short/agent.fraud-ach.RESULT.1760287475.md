```json
{
  "id": "8effc57d5383daa7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287475,
  "host_pid": "9e6742732c60:1",
  "hash": "257a33571fe5cc6cbacf2715a567ba14450aef39b9e1d0814e585aa0e3ed740f",
  "cid": "QmV1257a33571fe5cc6cbacf2715a567ba14450aef39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287475,
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
      "evaluated_at": 1760287475
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
  "sig": "85e947364fce604f529bae649ee67fa40a4fd59d981de7d90dab95ed825bb0d8"
}
```

Fraud detected: invalid_routing (score: 84)
Transaction: 357223800655087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 10373843, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}