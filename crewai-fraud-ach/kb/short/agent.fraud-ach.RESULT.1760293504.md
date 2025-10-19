```json
{
  "id": "9ac120b9c5f639c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293504,
  "host_pid": "9e6742732c60:1",
  "hash": "f37c5f53bc7aba467cfaa8dff5691e1f7994b4e658d89e26fff26a6defe14433",
  "cid": "QmV1f37c5f53bc7aba467cfaa8dff5691e1f7994b4e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293504,
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
      "evaluated_at": 1760293504
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
  "sig": "71a255752ae6f8db20242b7dddded09c8309c2edc3939fb3d7da87da9baccad2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 730896563459202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 78981540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'b6a475fea2d998c5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}