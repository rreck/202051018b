```json
{
  "id": "6303c4435ce6e89e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287813,
  "host_pid": "9e6742732c60:1",
  "hash": "479450ec55e6b25047648b94036d7395323dd755026601050ebf7bd8caa70890",
  "cid": "QmV1479450ec55e6b25047648b94036d7395323dd755",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287813,
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
      "evaluated_at": 1760287813
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
  "sig": "fc584249c9ddb1c6f91bd36c40d1aec3e5b410ff2a59356e6eb0cb1989fb05a8"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 111000025262531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 23257070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': 'cd477724f7ce5ce7'}}}