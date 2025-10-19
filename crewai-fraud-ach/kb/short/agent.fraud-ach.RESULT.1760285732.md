```json
{
  "id": "efddb8517c213ecf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285732,
  "host_pid": "9e6742732c60:1",
  "hash": "a3e3eccc45aa3e06d6804913d1ae5091125594c3d26052d50f22fd5c1c7e7da8",
  "cid": "QmV1a3e3eccc45aa3e06d6804913d1ae5091125594c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285732,
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
      "evaluated_at": 1760285732
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
  "sig": "609a2d66fcb2742dc9b66504384e462ec2cad7ef34eadd495c7a340ac169ae7b"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 021000026697062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 23626572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}