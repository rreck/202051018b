```json
{
  "id": "cc60535bc57410d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289904,
  "host_pid": "9e6742732c60:1",
  "hash": "d9be860f0e56355c534110f70666a8b310a6084783b948f0a369e4018de82984",
  "cid": "QmV1d9be860f0e56355c534110f70666a8b310a60847",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289904,
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
      "evaluated_at": 1760289904
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
  "sig": "60681a9ace6971a4132e54e118d3c0a3a4242170218d69d2e42e0de297d54351"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 67700928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}