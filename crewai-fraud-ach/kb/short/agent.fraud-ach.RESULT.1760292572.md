```json
{
  "id": "f7cb87cee8e23a5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292572,
  "host_pid": "9e6742732c60:1",
  "hash": "cab7ea597f702ac1ec2bb1be04afbe48b3351f32f5043f7ba92b0e77f4657ad3",
  "cid": "QmV1cab7ea597f702ac1ec2bb1be04afbe48b3351f32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292572,
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
      "evaluated_at": 1760292572
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
  "sig": "0f1f56d52155ba495a1241c759fa7bfb1d5d2495a9fcdad4966fbe41af5b108b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039404283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 66875400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}