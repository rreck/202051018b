```json
{
  "id": "7ef3c05f6e712fcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287191,
  "host_pid": "9e6742732c60:1",
  "hash": "5eb9b4098fcf3d89543a50ec1d6f7abbc4d5ea1d1d96cb78ca39ef091a9ddd27",
  "cid": "QmV15eb9b4098fcf3d89543a50ec1d6f7abbc4d5ea1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287191,
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
      "evaluated_at": 1760287191
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
  "sig": "901f9987b86cc2b76f48260fb22d62f3d7344c16dd47be7e14cb030acd6c932d"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 15356610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}