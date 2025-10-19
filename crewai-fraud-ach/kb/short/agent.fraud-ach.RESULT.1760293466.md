```json
{
  "id": "15c97952b689eef7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293466,
  "host_pid": "9e6742732c60:1",
  "hash": "17c1e89c4807030b68d33f0c67f3b448508fb29312a3c5c05e91c4c0e24cb361",
  "cid": "QmV117c1e89c4807030b68d33f0c67f3b448508fb293",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293466,
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
      "evaluated_at": 1760293466
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
  "sig": "ae56c0605deda975a79db1141bfcaf5f65ae7bd0aa421968ad3314f72099b065"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 118929074583077
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 48658515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': '9c7c32bd8fa37035'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}