```json
{
  "id": "3808a9d87135c2c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289464,
  "host_pid": "9e6742732c60:1",
  "hash": "a2f0e3b5391ea3b5912121a61764a33fe08c773ebbaddd941556d8f4c98fa7bd",
  "cid": "QmV1a2f0e3b5391ea3b5912121a61764a33fe08c773e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289464,
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
      "evaluated_at": 1760289464
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
  "sig": "ff64adfd6921fe7f81d70f321ad68e2828bf3016e6722eba686c59dee96bacbc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033386526
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 18035552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285764, 'matching_hash': 'a3ad727f5ed38962'}}}