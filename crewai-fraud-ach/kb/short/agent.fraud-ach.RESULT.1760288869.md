```json
{
  "id": "8abd8dbefb08433f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288869,
  "host_pid": "9e6742732c60:1",
  "hash": "09ada09d52652a3d9d64a0484f37fd3cde7ac6fc1b1f4271bb5ac46030d21fe5",
  "cid": "QmV109ada09d52652a3d9d64a0484f37fd3cde7ac6fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288869,
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
      "evaluated_at": 1760288869
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
  "sig": "21cca6ace3b974f7e60a0cb7af7c1f7cf332bc8e45f06097159236040451c86d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 39614850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}