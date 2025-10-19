```json
{
  "id": "f1cf0b494b2b3114",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291032,
  "host_pid": "9e6742732c60:1",
  "hash": "7a6c795ee240c78c25f4d79dea340fbea714798233055b42bfdf80062bf3f0e5",
  "cid": "QmV17a6c795ee240c78c25f4d79dea340fbea7147982",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291032,
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
      "evaluated_at": 1760291032
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
  "sig": "31185154cf643e4b0eba2044ac3ea22a73615a4aa04b6f7df74c478d81ac23bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468256911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 29951130, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': 'b0ec3a54cf0504a9'}}}