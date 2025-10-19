```json
{
  "id": "a875b10c474be017",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293177,
  "host_pid": "9e6742732c60:1",
  "hash": "4b4a71630b271469628e3ab71ac1d7a67e63bc81473310b58b2d081a5c0c93ed",
  "cid": "QmV14b4a71630b271469628e3ab71ac1d7a67e63bc81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293177,
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
      "evaluated_at": 1760293177
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
  "sig": "63dc75a64a6328a44d045afba2c898912025c14d77280d962fe3fc4b8f69f41e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272525723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 19526136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '7f6b158faad48b99'}}}