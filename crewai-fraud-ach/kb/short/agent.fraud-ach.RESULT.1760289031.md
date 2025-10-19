```json
{
  "id": "0522daa4ed1423aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289031,
  "host_pid": "9e6742732c60:1",
  "hash": "66305cea0c69c4dc46a9b1e87b7ea1cc8cfb4c8d440dd4d9d5c83ad38c6bed10",
  "cid": "QmV166305cea0c69c4dc46a9b1e87b7ea1cc8cfb4c8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289031,
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
      "evaluated_at": 1760289031
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
  "sig": "5fe76af2c3e3c0b45774dba41ebe83770aa47bbe271011cfa4c549d21e9732d5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 763245925890246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 50403435, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': '634500dd7ac761f0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '763245921', 'validation_error': 'Invalid routing number checksum'}}}