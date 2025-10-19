```json
{
  "id": "76f8fab9700e9da3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292450,
  "host_pid": "9e6742732c60:1",
  "hash": "c8960fb8ff422d57a129888fba0cbd2092496d24c362cb4c22c9f2a550e2c8d1",
  "cid": "QmV1c8960fb8ff422d57a129888fba0cbd2092496d24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292450,
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
      "evaluated_at": 1760292450
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
  "sig": "54e5dcdd8d5821dc01d1dc43495915e84acad7abab6f468181f677fb8fda57ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246128124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 49500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'd8f9033e4ee0a57f'}}}