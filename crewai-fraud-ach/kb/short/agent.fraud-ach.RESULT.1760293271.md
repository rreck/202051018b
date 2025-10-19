```json
{
  "id": "a253caf40435442b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293271,
  "host_pid": "9e6742732c60:1",
  "hash": "85892e6f989e9c62ae0a3b71a0f0f6681d9bb00ba8392d8763a66e6eabd5a71d",
  "cid": "QmV185892e6f989e9c62ae0a3b71a0f0f6681d9bb00b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293271,
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
      "evaluated_at": 1760293271
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
  "sig": "f84537bc06f2f06c71144bb4a4e71d1bed6d871497617d102b598e8efd634414"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 691661796885470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 22113180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': 'c2d09785100b76ca'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}