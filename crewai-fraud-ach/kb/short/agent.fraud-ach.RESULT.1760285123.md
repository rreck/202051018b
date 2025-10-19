```json
{
  "id": "f778256b8f731c17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285123,
  "host_pid": "9e6742732c60:1",
  "hash": "62d030c2160fdcd79b48698c6683fe14a684ec58af82570af4ec2d45d6100be9",
  "cid": "QmV162d030c2160fdcd79b48698c6683fe14a684ec58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285123,
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
      "evaluated_at": 1760285123
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
  "sig": "533d9b032594542b8e86e4050e3af634146b7ff43d08d96fbbdea50741903e19"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100275531952
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760284979, 'matching_hash': '283eac5c65a068f4'}}}