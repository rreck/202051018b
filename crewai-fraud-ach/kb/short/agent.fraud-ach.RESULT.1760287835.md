```json
{
  "id": "1dde2a0d2099abee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287835,
  "host_pid": "9e6742732c60:1",
  "hash": "c0113b6b04bddcf3130e7501278284026782df5a2ec215d5fa0ebd45462a8c92",
  "cid": "QmV1c0113b6b04bddcf3130e7501278284026782df5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287835,
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
      "evaluated_at": 1760287835
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
  "sig": "b2c8476d935590fb10a4f5ff64aa7f4555b0b76819dcdcba5817f47f4d23c482"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 111000025810032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 36242166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '4a1b4df87be22a11'}}}