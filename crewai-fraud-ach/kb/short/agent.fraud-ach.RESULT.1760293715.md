```json
{
  "id": "782644526ecfe55c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293715,
  "host_pid": "9e6742732c60:1",
  "hash": "a2b8cc9a8e314f59d853c18b9f2f59dd1b7eff1eeb43fe33e45a9f507947e55a",
  "cid": "QmV1a2b8cc9a8e314f59d853c18b9f2f59dd1b7eff1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293715,
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
      "evaluated_at": 1760293715
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
  "sig": "df9c9e0854342f193096a31f966b9514bf5b501d5f577e1e5c6cb749203d5212"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 118929074583077
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 49769440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': '9c7c32bd8fa37035'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}