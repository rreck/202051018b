```json
{
  "id": "54a10c2e2f01a153",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291505,
  "host_pid": "9e6742732c60:1",
  "hash": "464f7ea21937e2dbe97534a7d57a4c24d78ebbc19a08db9734d1a73c0029929b",
  "cid": "QmV1464f7ea21937e2dbe97534a7d57a4c24d78ebbc1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291505,
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
      "evaluated_at": 1760291505
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
  "sig": "fd529a2b6900cf19b32add9ceff6c9f549a1264d36d54c666b51b3442b7d1ba7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 357223800655087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 29931088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}