```json
{
  "id": "b59f0b4ae7cfe926",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293956,
  "host_pid": "9e6742732c60:1",
  "hash": "4e835e38f346fcc555a7ae7a6afffbbbab0a3f2f503daf6871ac1cd5da6fcdf5",
  "cid": "QmV14e835e38f346fcc555a7ae7a6afffbbbab0a3f2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293956,
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
      "evaluated_at": 1760293956
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
  "sig": "550fe08df7397c7c572765c6fcfc070c067c02a3a9b5da69212ae6760ca21cef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 50219929, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}