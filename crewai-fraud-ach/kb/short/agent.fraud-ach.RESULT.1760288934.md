```json
{
  "id": "81a35d4987460854",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288934,
  "host_pid": "9e6742732c60:1",
  "hash": "3e2230a5c717f171be5be07eaa45b88efc4e6a2587b078e1a6805eb3196ca1f8",
  "cid": "QmV13e2230a5c717f171be5be07eaa45b88efc4e6a25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288934,
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
      "evaluated_at": 1760288934
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
  "sig": "18549f5b25f3f5ab633c1dbae5709225c82df84b309b98af47b482b72e04d1f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153543170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 10343700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}