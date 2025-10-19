```json
{
  "id": "a091f4b6aac9b69a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291535,
  "host_pid": "9e6742732c60:1",
  "hash": "54eb87ee0bef5be99dd0a83e71ad26cbe9b2915e9ddbb8b6f393d73d2b6b1c01",
  "cid": "QmV154eb87ee0bef5be99dd0a83e71ad26cbe9b2915e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291535,
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
      "evaluated_at": 1760291535
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
  "sig": "8c455340dc16f47988a131f1bdab67cea6c52cd4f9c3a904f8e1cb2966334289"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 19534782, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}