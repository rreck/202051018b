```json
{
  "id": "1162b71c7d4248ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294786,
  "host_pid": "9e6742732c60:1",
  "hash": "481521921ed206fc775aecac6344291b6d6b76f560cec733e4cbb01ae73a5025",
  "cid": "QmV1481521921ed206fc775aecac6344291b6d6b76f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294786,
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
      "evaluated_at": 1760294786
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
  "sig": "2414dc995e0f0ea7ebf56ec6532acbaadcd5fe81a39f3835ea52367c2b919e5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 77592976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}