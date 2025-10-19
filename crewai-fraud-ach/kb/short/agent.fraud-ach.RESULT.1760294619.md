```json
{
  "id": "9a82cc1e0433924a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294619,
  "host_pid": "9e6742732c60:1",
  "hash": "d9abdaf13d273477f9312682cfb863af34f1b1f15cb52df5659489eb24e6eb97",
  "cid": "QmV1d9abdaf13d273477f9312682cfb863af34f1b1f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294619,
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
      "evaluated_at": 1760294619
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
  "sig": "16aa457497701a14010bba7039a723a11a828af1003aa91ae61f1fb45590012c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 18226830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}