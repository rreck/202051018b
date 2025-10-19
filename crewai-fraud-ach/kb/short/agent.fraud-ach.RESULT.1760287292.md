```json
{
  "id": "e6fb347a29862f77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287292,
  "host_pid": "9e6742732c60:1",
  "hash": "80d688d4637460f1330018d903ea416da58d680915ebb70daa911c9707d98afd",
  "cid": "QmV180d688d4637460f1330018d903ea416da58d6809",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287292,
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
      "evaluated_at": 1760287292
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
  "sig": "d211e7554d45f3e3be1a4a9c3f3285428f84cc32ef51c98e4f2bec4971696bfe"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009596354415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 15308425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': 'f20df65cb297838c'}}}