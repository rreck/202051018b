```json
{
  "id": "49a8a0f87fa9cec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287905,
  "host_pid": "9e6742732c60:1",
  "hash": "be3ad88ceca8eddf93d8c564f2411ae86611ce90bf67191837e4555b29461293",
  "cid": "QmV1be3ad88ceca8eddf93d8c564f2411ae86611ce90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287905,
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
      "evaluated_at": 1760287905
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
  "sig": "c97ad3a7aa83c1a2402077cc04ea6cd13c4eb7b33fc6cfd511b5053a40efaa1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 25920408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}