```json
{
  "id": "b25b2d8a6058ca6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287775,
  "host_pid": "9e6742732c60:1",
  "hash": "0ec954175a80c6de6c0d4d6f7b5b81e1417826e7fb152e03fda9e479ff7ee8e0",
  "cid": "QmV10ec954175a80c6de6c0d4d6f7b5b81e1417826e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287775,
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
      "evaluated_at": 1760287775
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
  "sig": "f345a2237d18b1098c37928b589e445b97848bc454996a350d83c530029d9f82"
}
```

Fraud detected: invalid_routing (score: 91)
Transaction: 408733730305741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 29229984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '77eebc6eb9f79eeb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}