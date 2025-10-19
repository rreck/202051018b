```json
{
  "id": "6d0787b2fa0811f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288464,
  "host_pid": "9e6742732c60:1",
  "hash": "fb3d32bf513608cd1703e53d433442f2cd2b9c63c86ffc2ec2312c2b3f2805b3",
  "cid": "QmV1fb3d32bf513608cd1703e53d433442f2cd2b9c63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288464,
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
      "evaluated_at": 1760288464
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
  "sig": "97b5b2bb4dd45914efa676b9e3297e8aab544f81590f68380fdb4b618e844d5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}284979, 'matching_hash': '6a7cc3d9f67da590'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}