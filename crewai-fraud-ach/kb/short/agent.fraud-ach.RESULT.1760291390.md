```json
{
  "id": "6d3e9633b7a3d3a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291390,
  "host_pid": "9e6742732c60:1",
  "hash": "ee477fb4bdfc279cb3e8ad9c21c61fc5e2ef2e4751825c3f9e38c1cb6b7ad4d6",
  "cid": "QmV1ee477fb4bdfc279cb3e8ad9c21c61fc5e2ef2e47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291390,
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
      "evaluated_at": 1760291390
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "8d598d9b7c6d90e4da1f2653ab26848d937f47e99e354671aa6799d8329883af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460168239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 14314806, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'c8b812a49265f53e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}