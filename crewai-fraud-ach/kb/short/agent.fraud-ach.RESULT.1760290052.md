```json
{
  "id": "f0734f26f5a69cb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290052,
  "host_pid": "9e6742732c60:1",
  "hash": "32d286607ee520b504209ff14da714b8ae0a71e8dd60c7119bebb46c7b0bcae4",
  "cid": "QmV132d286607ee520b504209ff14da714b8ae0a71e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290052,
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
      "evaluated_at": 1760290052
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
  "sig": "f3c6a4726034b8f57aa0121548df9c62b18ed70d1281f58968f697ee5965965a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 15451240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}