```json
{
  "id": "272445516b6c4a73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287991,
  "host_pid": "9e6742732c60:1",
  "hash": "b5f7d681e34550720a47f324f2441b492c275a662d9cf10bab8a9b22b1f60949",
  "cid": "QmV1b5f7d681e34550720a47f324f2441b492c275a66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287991,
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
      "evaluated_at": 1760287991
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
  "sig": "59d0ba5275e0de2775985d1fb4237c3ae4f790ce84fac4d59cbd13bd38ca4f1d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 529024316192383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 19989449, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285764, 'matching_hash': 'dc6c8a77c50d9997'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '529024315', 'validation_error': 'Invalid routing number checksum'}}}