```json
{
  "id": "02c868217704e108",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294430,
  "host_pid": "9e6742732c60:1",
  "hash": "4bd11854ed4c7ae19d941cecfd818a929e372a929c3aadd369bbb90b43af1b3b",
  "cid": "QmV14bd11854ed4c7ae19d941cecfd818a929e372a92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294430,
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
      "evaluated_at": 1760294430
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
  "sig": "7d76dee14ccb3d1e0bd2cfd8d172bf14846614cc67cb2b8de5ebc9b2f2c9ba65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246128124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 59500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'd8f9033e4ee0a57f'}}}