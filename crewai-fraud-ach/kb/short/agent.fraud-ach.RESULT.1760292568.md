```json
{
  "id": "5fa4585940450d67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292568,
  "host_pid": "9e6742732c60:1",
  "hash": "c8a582e44e78664b4aed1dba8a459942b03eb7edf71d65402d44a544883178a0",
  "cid": "QmV1c8a582e44e78664b4aed1dba8a459942b03eb7ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292568,
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
      "evaluated_at": 1760292568
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
  "sig": "1efbf95c672d1d0d4cb5dbdbedcecb3fa280cf013b2b000085de3f1bc8a7c98a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029513246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 10130400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': '556e5d87a3998e0a'}}}