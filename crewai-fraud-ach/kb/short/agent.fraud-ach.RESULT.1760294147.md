```json
{
  "id": "aaa409334fbcb97e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294147,
  "host_pid": "9e6742732c60:1",
  "hash": "5e93087bae7ce611c714304739962c3d16728d559c0b834aee56e728bc5956e0",
  "cid": "QmV15e93087bae7ce611c714304739962c3d16728d55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294147,
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
      "evaluated_at": 1760294147
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
  "sig": "a2de8a6f99b718488c3b387e05e60467c0a0e189f28334964015129e71bc8a8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 19167376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}