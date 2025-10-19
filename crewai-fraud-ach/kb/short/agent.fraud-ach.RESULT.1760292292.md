```json
{
  "id": "95e0c6807b9034cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292292,
  "host_pid": "9e6742732c60:1",
  "hash": "a9a917f33d349bd07817a04272e0b3319a1188dc136c67c14360bd8fbc48e6e4",
  "cid": "QmV1a9a917f33d349bd07817a04272e0b3319a1188dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292292,
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
      "evaluated_at": 1760292292
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
  "sig": "796dd7013a5673a59fbdd15e8b3e624a6455b4e95c982e3f5e509df883047a7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240953214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 11502066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': 'cfdb33c4cfd6ba9b'}}}