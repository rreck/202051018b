```json
{
  "id": "10b93f60eea640a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289101,
  "host_pid": "9e6742732c60:1",
  "hash": "c422ce46d47ea0ba0b8ba87108f0426ab2e2fd4468fce3a666880b4b792d2db4",
  "cid": "QmV1c422ce46d47ea0ba0b8ba87108f0426ab2e2fd44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289101,
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
      "evaluated_at": 1760289101
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
  "sig": "63dbc54f6bea61a355d6849755cc577e995b19c2540486b6c09bf6729bbdbde5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 45360686, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}