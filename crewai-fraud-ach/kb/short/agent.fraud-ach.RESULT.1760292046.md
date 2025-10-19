```json
{
  "id": "35815428cbec0d31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292046,
  "host_pid": "9e6742732c60:1",
  "hash": "b523bfd8bcf5c1c34af855b37ff0b3d5f65e6a8343e9f9d902dbfeeb4ee5ef06",
  "cid": "QmV1b523bfd8bcf5c1c34af855b37ff0b3d5f65e6a83",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292046,
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
      "evaluated_at": 1760292046
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
  "sig": "f733518829e6afbd6c8a78ad360e859f4e48fb70d83fb03fc93b60e5b0ec2e8a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 472304306013162
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 85671243, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '18e6c75ff941397c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}