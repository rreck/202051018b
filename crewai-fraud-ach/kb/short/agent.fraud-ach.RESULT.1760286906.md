```json
{
  "id": "1640da696c780937",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286906,
  "host_pid": "9e6742732c60:1",
  "hash": "95e7df3e90b85df8bf7f91e3ca78e4b065486646a13608cf271dd6386ded4752",
  "cid": "QmV195e7df3e90b85df8bf7f91e3ca78e4b065486646",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286906,
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
      "evaluated_at": 1760286906
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
  "sig": "7378c6ac636591e821ac2b672aa5549838e2621d6cfe3d5985bcb58cf4167d8b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000240022849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13671532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}