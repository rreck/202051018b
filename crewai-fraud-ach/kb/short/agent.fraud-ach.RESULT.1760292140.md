```json
{
  "id": "f11be36bd30f7a80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292140,
  "host_pid": "9e6742732c60:1",
  "hash": "dc7d4f50c64fe0dcc2e69e4dc608b42f0f63626b60aaa1b02d4401e998b2dabd",
  "cid": "QmV1dc7d4f50c64fe0dcc2e69e4dc608b42f0f63626b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292140,
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
      "evaluated_at": 1760292140
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
  "sig": "fac6f825b3476424b75220e85c3984bfba0d5bc645250d550e2129b26261942c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248536916
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 28149389, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285764, 'matching_hash': '45170da297af1bde'}}}