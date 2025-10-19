```json
{
  "id": "2fcb48c7ddff5254",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294226,
  "host_pid": "9e6742732c60:1",
  "hash": "1a2516c6b9f9b5c9788dc5cb7dd9eae5b856f8043c9e3798abcad521bb415ffd",
  "cid": "QmV11a2516c6b9f9b5c9788dc5cb7dd9eae5b856f804",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294226,
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
      "evaluated_at": 1760294226
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
  "sig": "faee80c3dd9893654c037982e874dcb48e585696f409a32bd017a2e66d1ea2eb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 304701772219564
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 55931850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}nds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6665760}}}