```json
{
  "id": "6a66d37258735b3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294276,
  "host_pid": "9e6742732c60:1",
  "hash": "564ccad9e37594475fffb633245dbb1d7329a50d2471c79eecfd0f0c1311c474",
  "cid": "QmV1564ccad9e37594475fffb633245dbb1d7329a50d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294276,
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
      "evaluated_at": 1760294276
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
  "sig": "1155dc4287ec36247ea10889598bec03f653663f505bb7fed3f47d48b63fb00c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 069024451692491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 50035965, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '560f842b4bd5b95e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6875376}}}