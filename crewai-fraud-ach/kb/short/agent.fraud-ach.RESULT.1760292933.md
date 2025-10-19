```json
{
  "id": "465378e56f1a9432",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292933,
  "host_pid": "9e6742732c60:1",
  "hash": "920b94b27fcc23301fa24cd85304585ff3dcc90b3412ea1e84986dde11ea5db3",
  "cid": "QmV1920b94b27fcc23301fa24cd85304585ff3dcc90b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292933,
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
      "evaluated_at": 1760292933
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
  "sig": "9e0a8789e34905b929100022c20c2980a85696f5423ecdb75192834c0d7d7419"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 19474208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}