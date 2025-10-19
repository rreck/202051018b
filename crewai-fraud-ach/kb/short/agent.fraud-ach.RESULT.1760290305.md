```json
{
  "id": "a9a9839cd34a61ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290305,
  "host_pid": "9e6742732c60:1",
  "hash": "150ddfe4fc2e10b94437279077ff3af06d74e7795c1fd728fbd25b6abf9e2740",
  "cid": "QmV1150ddfe4fc2e10b94437279077ff3af06d74e779",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290305,
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
      "evaluated_at": 1760290305
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
  "sig": "fa2adca2d6b923a27618edc623baf0b4e7c74dd4dc7a8e7e61ddbba5dd4de78d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244096993316032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 38200008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}