```json
{
  "id": "352e086cab4c7a1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289571,
  "host_pid": "9e6742732c60:1",
  "hash": "03514927bff20603b7bd2392ef789677f65e11a7aa59efb693957643498ef0bc",
  "cid": "QmV103514927bff20603b7bd2392ef789677f65e11a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289571,
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
      "evaluated_at": 1760289571
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
  "sig": "8726d680e0c5eab0496a9105acaf256a4799fc064c7469a2b7df0dac1d0590cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240515775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 30285309, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}