```json
{
  "id": "89690ddb36a3baca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294274,
  "host_pid": "9e6742732c60:1",
  "hash": "fa21c1fd77c127553f12dccb43154503876c8abec99e2f1ca3091e8fc6c1041d",
  "cid": "QmV1fa21c1fd77c127553f12dccb43154503876c8abe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294274,
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
      "evaluated_at": 1760294274
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
  "sig": "87bd226d32de4b8d1cb973e11e647e5733c00cab09241c4a8202ba5cb2746bd8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 041887157928370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 102216305, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '40835df504bb3fdd'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}