```json
{
  "id": "a026fd650bb073d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291461,
  "host_pid": "9e6742732c60:1",
  "hash": "db90873110a4152e78649b30e085feab7489e02c1afb9f7b5c735dc9dd619c6f",
  "cid": "QmV1db90873110a4152e78649b30e085feab7489e02c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291461,
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
      "evaluated_at": 1760291461
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
  "sig": "097b9986d332d2fc110bc5119dbefff3d35d2f39488d1ef33651997c495f9ccf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 17713850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}