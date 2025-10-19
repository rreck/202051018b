```json
{
  "id": "99147b918c45709a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291196,
  "host_pid": "9e6742732c60:1",
  "hash": "1a0605a69431a35fc79afbfa4ad08d141a79d6dff8e308e5bad3098648e0d893",
  "cid": "QmV11a0605a69431a35fc79afbfa4ad08d141a79d6df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291196,
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
      "evaluated_at": 1760291196
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
  "sig": "6138f0c615b415806679f9803c87e160eab6aa5128ea333bf6e2dc0361912cc0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 676666911893287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 65902902, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '67218afda9e45d8d'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}