```json
{
  "id": "62bb37fbfb8c95f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289660,
  "host_pid": "9e6742732c60:1",
  "hash": "71d38c69fd9fd919d20ff047952b0571616ac04afa76d9806168fb3fc17e53ce",
  "cid": "QmV171d38c69fd9fd919d20ff047952b0571616ac04a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289660,
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
      "evaluated_at": 1760289660
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
  "sig": "ba529d8ce70d96b41da8192aa3526a157517028adf31493000f8f8456bdc08bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033294426
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 18654690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '591497f4da3dc787'}}}