```json
{
  "id": "af43bf6177b02dd7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288455,
  "host_pid": "9e6742732c60:1",
  "hash": "3ea3aa9696910be50daf9d0fba9e6262091f1c3dee7340f6e90ff5be634e435e",
  "cid": "QmV13ea3aa9696910be50daf9d0fba9e6262091f1c3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288455,
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
      "evaluated_at": 1760288455
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
  "sig": "cab2c35bf34948224b2c969ea5956c2553fb41bfccf1e141dec6f445e628c55b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025810032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 46037346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '4a1b4df87be22a11'}}}