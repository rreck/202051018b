```json
{
  "id": "42e9a365766bd515",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288571,
  "host_pid": "9e6742732c60:1",
  "hash": "a51ba196519a23ed4d00809884da6ac0843177141d87d51d5b93b30805442f4d",
  "cid": "QmV1a51ba196519a23ed4d00809884da6ac084317714",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288571,
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
      "evaluated_at": 1760288571
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
  "sig": "32296fcc4b1405ba64a7dd9684405fa20b686462d37d9b930ce6415c0b42fe68"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 845955323982908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 35012538, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': '603efe89834eadf7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '845955329', 'validation_error': 'Invalid routing number checksum'}}}