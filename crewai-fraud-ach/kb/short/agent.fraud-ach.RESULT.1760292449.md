```json
{
  "id": "e52942e8f12a7b01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292449,
  "host_pid": "9e6742732c60:1",
  "hash": "725b68bd4fb5af0f3195e74cdbe440b7f62d20d0764e68601e850f1bcbabbbd9",
  "cid": "QmV1725b68bd4fb5af0f3195e74cdbe440b7f62d20d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292449,
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
      "evaluated_at": 1760292449
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
  "sig": "d9207de4e1ec924e6ea0f0472e45040527e7465e9212f15c014e464dfa389da6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 24833952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}