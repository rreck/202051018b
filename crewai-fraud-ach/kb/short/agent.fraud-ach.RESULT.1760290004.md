```json
{
  "id": "05eb3c4f6f9c21b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290004,
  "host_pid": "9e6742732c60:1",
  "hash": "19404b0ad83256ff3fc4a763a22d0d9707df759e99a865e748fa095527b7231e",
  "cid": "QmV119404b0ad83256ff3fc4a763a22d0d9707df759e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290004,
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
      "evaluated_at": 1760290005
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
  "sig": "61817b67daf9f05a8d601ea0a6503f18e6bbb7eeba74e025b0d2c020f6cdb6ec"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 013419647478508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 35209812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': 'f6be81dddddc1883'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}