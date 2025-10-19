```json
{
  "id": "7676b4de8ccf0bac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290114,
  "host_pid": "9e6742732c60:1",
  "hash": "9a0a5f0991bcf4496716588b2774eec25c0a7e383e1211043b4ad815af73f9e4",
  "cid": "QmV19a0a5f0991bcf4496716588b2774eec25c0a7e38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290114,
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
      "evaluated_at": 1760290114
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
  "sig": "d2f2d7fec53df7a611b4b6e25bfd6a7e0bbfd3367312cfe5f16b8095ad398927"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 864091464204372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 33599898, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '74f25dd839f89a8f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}