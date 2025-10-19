```json
{
  "id": "d496104b09cf5209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290636,
  "host_pid": "9e6742732c60:1",
  "hash": "91ec105cf9c4be5f87d0bf4c510ea791e8c7c76d0d62bec1e0c54cb2132e06cf",
  "cid": "QmV191ec105cf9c4be5f87d0bf4c510ea791e8c7c76d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290636,
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
      "evaluated_at": 1760290636
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
  "sig": "b31fb1997dc42b3f3d142946cd4a91c262d2b654580061c8bf5cedccb44ef24c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 52487495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}