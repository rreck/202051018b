```json
{
  "id": "7c1526b3ef38b583",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286457,
  "host_pid": "9e6742732c60:1",
  "hash": "e0b48e2f346ca8e2cefe065616ac8505eaa417b13dd7f561ca20f2f3eebe1ec2",
  "cid": "QmV1e0b48e2f346ca8e2cefe065616ac8505eaa417b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286457,
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
      "evaluated_at": 1760286457
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a05e241b38fda6485b0c8522c5a355ac55176282d7f9d64080d962deb0272452"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598219972
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12713038, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '09b5d296b49f9602'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}