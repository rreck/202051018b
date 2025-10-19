```json
{
  "id": "8e82c2e546105fe7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294448,
  "host_pid": "9e6742732c60:1",
  "hash": "3ec99bbff30ff13c7d4219a2775ff87baac487329ec787bada73bfa90da63f4d",
  "cid": "QmV13ec99bbff30ff13c7d4219a2775ff87baac48732",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294448,
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
      "evaluated_at": 1760294448
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
  "sig": "d95c58bb2fcb037b4c2a8722d7a46833b0515b8f12a5bddde629b4250cfdd8c3"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 834096557545062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 80765300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': 'c4c3f7a3fe4b8b75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}