```json
{
  "id": "03b480ca6d56c45f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293180,
  "host_pid": "9e6742732c60:1",
  "hash": "b76b40db8dda2988d20ab2c2662f5551b995eb5867c0f37c946731b467723567",
  "cid": "QmV1b76b40db8dda2988d20ab2c2662f5551b995eb58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293180,
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
      "evaluated_at": 1760293180
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
  "sig": "31199fb4df164fc722a47cd32ac40a12e5087783bede969dc6d4243759813292"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 105867816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}