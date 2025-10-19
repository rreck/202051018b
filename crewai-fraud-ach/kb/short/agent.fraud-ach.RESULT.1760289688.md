```json
{
  "id": "a08ce6d72c82327e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289688,
  "host_pid": "9e6742732c60:1",
  "hash": "5613889063269ebce2972c60931dab71985b7926827a5d797cae5e4526eb88d5",
  "cid": "QmV15613889063269ebce2972c60931dab71985b7926",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289688,
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
      "evaluated_at": 1760289688
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
  "sig": "027b8252c151c989c7a9b6dd857dcf33c7e0c359dcd8bdd9adbf14f86e483920"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020048209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 10810150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': '08bd6998776e568a'}}}