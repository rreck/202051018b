```json
{
  "id": "2f35395c571f848f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289890,
  "host_pid": "9e6742732c60:1",
  "hash": "a4f968dd6bee1eec045f2f9c5a8c372ef484238794e8fa7160396274de56d3bc",
  "cid": "QmV1a4f968dd6bee1eec045f2f9c5a8c372ef4842387",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289890,
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
      "evaluated_at": 1760289890
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
  "sig": "a0a1ba31a5eae555eb599daf0530897d15ee7ff93e9b2e0b9c188fcf62ebd2dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460250809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 57258448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'b939c4c4097f2f1f'}}}