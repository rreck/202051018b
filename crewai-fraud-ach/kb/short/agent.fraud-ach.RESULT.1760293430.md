```json
{
  "id": "98a0944fde15de05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293430,
  "host_pid": "9e6742732c60:1",
  "hash": "9286f25c1fc0a835f2e4ea70ed70189945f0e64e6c6e754fbf4932b34238d335",
  "cid": "QmV19286f25c1fc0a835f2e4ea70ed70189945f0e64e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293430,
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
      "evaluated_at": 1760293430
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
  "sig": "966432380b4105f79dc44ad8e6370fe9c4e50bbcd7bb2859dcf83eebab7785ec"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 64242856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}