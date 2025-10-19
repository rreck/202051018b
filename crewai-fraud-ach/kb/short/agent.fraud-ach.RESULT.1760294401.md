```json
{
  "id": "99fdd2bdc4e4fb97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294401,
  "host_pid": "9e6742732c60:1",
  "hash": "bcd2414eb53d8d70a66b15a0ecea3786aa014863781d1e375a75dd121d5b8e7c",
  "cid": "QmV1bcd2414eb53d8d70a66b15a0ecea3786aa014863",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294401,
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
      "evaluated_at": 1760294401
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "68d461337dbdb38efd8ad7f41ae71abf2ff1e0069650b79bfdc0ef2ff9fffd2d"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000027783297
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 118500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '92df9dc264d0d07b'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}