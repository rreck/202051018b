```json
{
  "id": "5072a1102e565d18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292706,
  "host_pid": "9e6742732c60:1",
  "hash": "930e2793a05c7714d8d0f03f22b1f2a18acc7fd9d57de979e3ffe31d7baa0d47",
  "cid": "QmV1930e2793a05c7714d8d0f03f22b1f2a18acc7fd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292706,
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
      "evaluated_at": 1760292706
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
  "sig": "0af784596a58c32fe256abff2608f33b4b28465f239589ff028bb9db902032bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026132147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 36822779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': 'fe0c58008e192989'}}}