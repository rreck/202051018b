```json
{
  "id": "ec896b097f287e95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285827,
  "host_pid": "9e6742732c60:1",
  "hash": "b1b9b7ff36c3ae27a45525518a257ffa1cb49d7f4e7e79f0f5b8cd34590219e2",
  "cid": "QmV1b1b9b7ff36c3ae27a45525518a257ffa1cb49d7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285827,
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
      "evaluated_at": 1760285827
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
  "sig": "f2f4b7d3caed870221ba5a7fd8e64bdb67e6132a82256ad1de521bbbd8581af8"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 478694940117269
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}