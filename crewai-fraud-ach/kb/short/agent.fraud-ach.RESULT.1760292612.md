```json
{
  "id": "7d70a6f3e82277fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292612,
  "host_pid": "9e6742732c60:1",
  "hash": "66ada359195a96593a2aaf5c8bb3870636aa6b4d8b7d3d3998e43bca2ea6b8b5",
  "cid": "QmV166ada359195a96593a2aaf5c8bb3870636aa6b4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292612,
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
      "evaluated_at": 1760292612
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
  "sig": "fda27fb818519f59a6b1e29fac52b3f1a66b93e012f998bca259886a77a225e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596807926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 65989908, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'efb59c040be3d116'}}}