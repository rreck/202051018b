```json
{
  "id": "f3900dbfbdc3babb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292264,
  "host_pid": "9e6742732c60:1",
  "hash": "905b9a3f75b06106dd2ff88ee4d0e27f20a098215d5bdde41c8d7d75edc980d9",
  "cid": "QmV1905b9a3f75b06106dd2ff88ee4d0e27f20a09821",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292264,
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
      "evaluated_at": 1760292264
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
  "sig": "722b8faa4c07075effb3b13bad8624eda145308e83e66fb0f0016192f2b4f2bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 45817562, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}