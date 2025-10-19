```json
{
  "id": "656de75abe2c1a5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286697,
  "host_pid": "9e6742732c60:1",
  "hash": "ce80ea63e6120312b716bf75ae43b9ad17c421407ddf4a5c3dca4b6bca532e57",
  "cid": "QmV1ce80ea63e6120312b716bf75ae43b9ad17c42140",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286697,
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
      "evaluated_at": 1760286697
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
  "sig": "9aae7eb3177c4ed5f2a3aeae129f1242425b744348fbe1eebc1f984f74c43309"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16146872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}