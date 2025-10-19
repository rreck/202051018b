```json
{
  "id": "44cf83284fafeeed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293440,
  "host_pid": "9e6742732c60:1",
  "hash": "1036f74503c062f89fd9bb016e4dbb16fd0f98ab13e403b2319fa2434d1ab674",
  "cid": "QmV11036f74503c062f89fd9bb016e4dbb16fd0f98ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293440,
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
      "evaluated_at": 1760293440
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
  "sig": "3bbd8ef6b5f6d1c51b1618353d137f470f854f6f3e22f3f9f7631afcbdf34f9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 94485342, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}