```json
{
  "id": "c2d8a9a6f396ded2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293286,
  "host_pid": "9e6742732c60:1",
  "hash": "d1515b8e84ee69f6b132300cbb9fe9a6f24184fb02420e907c9ba26d2c55b4ed",
  "cid": "QmV1d1515b8e84ee69f6b132300cbb9fe9a6f24184fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293286,
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
      "evaluated_at": 1760293286
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "71e8ed8bf6a5722c73f0a217a97a6493cd41e51f08ac554cd06339286ebfec85"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 107500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}