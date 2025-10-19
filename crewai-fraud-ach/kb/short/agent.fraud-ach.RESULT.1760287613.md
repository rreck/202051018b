```json
{
  "id": "a3fb6dc325bff7aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287613,
  "host_pid": "9e6742732c60:1",
  "hash": "844b0d1e3c3cad6acbc260ca6d7d0b606fb43f914f9590fde2de3478fc8c1f72",
  "cid": "QmV1844b0d1e3c3cad6acbc260ca6d7d0b606fb43f91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287613,
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
      "evaluated_at": 1760287613
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
  "sig": "3c9954ccf6dd26c6696ebd1aa0ffb44368d34b0ff3d0230e9d6809f775dc3fd0"
}
```

Fraud detected: invalid_routing (score: 87)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 19873260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}