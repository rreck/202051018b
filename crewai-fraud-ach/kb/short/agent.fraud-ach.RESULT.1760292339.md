```json
{
  "id": "d3e1db6c3754c813",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292339,
  "host_pid": "9e6742732c60:1",
  "hash": "1a582a9a627818fb1ff71d2d2ab8421fc802dd03dc09e37efd85005064af041e",
  "cid": "QmV11a582a9a627818fb1ff71d2d2ab8421fc802dd03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292339,
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
      "evaluated_at": 1760292339
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
  "sig": "1c368e75cdfdcffca830d0b675a03b517bef010860bb7a7db63a8629d9e714a4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 009592678117470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 23617230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': 'f5249213623024b2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '009592679', 'validation_error': 'Invalid routing number checksum'}}}