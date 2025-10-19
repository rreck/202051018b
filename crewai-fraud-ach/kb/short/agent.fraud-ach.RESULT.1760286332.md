```json
{
  "id": "324a3c6cf030d7bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286332,
  "host_pid": "9e6742732c60:1",
  "hash": "3d2bbefb7ad103aa9d29d9af51a8abd937d71c1513f88c6cab61b827c8eda260",
  "cid": "QmV13d2bbefb7ad103aa9d29d9af51a8abd937d71c15",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286332,
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
      "evaluated_at": 1760286332
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
  "sig": "3bb1396b3fe8e3f57cb17acfb0c777b9ae1a86d03e007bceeb4d7c10bddcb019"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031117260
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}