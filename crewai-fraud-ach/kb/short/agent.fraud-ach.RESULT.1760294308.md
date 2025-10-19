```json
{
  "id": "cfdba6204048319b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294308,
  "host_pid": "9e6742732c60:1",
  "hash": "937487f3d89559ca4ffc13613c59a8be5c1c76fab68be475e26a825591bd58c9",
  "cid": "QmV1937487f3d89559ca4ffc13613c59a8be5c1c76fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294308,
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
      "evaluated_at": 1760294308
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
  "sig": "db4d1de68bb826bb124457610e2c421fa1060fe58ef9020464dc03f27b7ebe50"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 357223800655087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 39964805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}