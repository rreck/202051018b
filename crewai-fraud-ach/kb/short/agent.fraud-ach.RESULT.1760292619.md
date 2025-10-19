```json
{
  "id": "c3a969742ba94aae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292619,
  "host_pid": "9e6742732c60:1",
  "hash": "056a3a4e93fc3a0afc01aaa706bb9af138f4abfb50be0fe4d18bcc6dd95fd80e",
  "cid": "QmV1056a3a4e93fc3a0afc01aaa706bb9af138f4abfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292619,
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
      "evaluated_at": 1760292619
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
  "sig": "513a790519998d0674b2bab6a47f0006a7afe2bfacd2a239ebc60da3912dea88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273742232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 42376227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '98264f1e6b5ab805'}}}