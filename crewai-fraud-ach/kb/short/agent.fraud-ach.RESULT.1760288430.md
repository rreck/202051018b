```json
{
  "id": "3a1c6a57302c3574",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288430,
  "host_pid": "9e6742732c60:1",
  "hash": "d4f9519b40b9daadbf94e868cd1c98383d2a97ff4cb7ae2ee86f4844c183241b",
  "cid": "QmV1d4f9519b40b9daadbf94e868cd1c98383d2a97ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288430,
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
      "evaluated_at": 1760288430
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
  "sig": "10a5f25a493950d7a6d9978748ae71df859ae96a38c4eebff4b4d7666f242052"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 053611743401753
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 18949680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': 'ed032d3a1e3d03a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}