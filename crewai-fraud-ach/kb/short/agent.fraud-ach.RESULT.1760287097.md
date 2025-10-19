```json
{
  "id": "aba7741057946de1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287097,
  "host_pid": "9e6742732c60:1",
  "hash": "bd59eb9a806ebdaa2e8ccac7995197e688be197cd9d414b6fc858775bc631e89",
  "cid": "QmV1bd59eb9a806ebdaa2e8ccac7995197e688be197c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287097,
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
      "evaluated_at": 1760287097
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
  "sig": "e4622a9c97c9e19052d50cc5b49aca7906ce7e2c683afc0d44c29ba88690af7c"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 529024316192383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12145488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285764, 'matching_hash': 'dc6c8a77c50d9997'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '529024315', 'validation_error': 'Invalid routing number checksum'}}}