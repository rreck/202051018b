```json
{
  "id": "5df338b70b994d76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291736,
  "host_pid": "9e6742732c60:1",
  "hash": "08c7be5239365fb8d71bfe6c6390f3fce99eb1387f20a1b4d004c2b5da33ca3b",
  "cid": "QmV108c7be5239365fb8d71bfe6c6390f3fce99eb138",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291736,
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
      "evaluated_at": 1760291736
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
  "sig": "85933e63c65fe5ceae9491468e6e96ee37d73338196425ed33b98d25a967e7c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032979175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 59619196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '92afbef802abc12c'}}}