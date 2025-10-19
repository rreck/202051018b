```json
{
  "id": "5bf6189f8713519b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287616,
  "host_pid": "9e6742732c60:1",
  "hash": "0f97f5f62d9d277d8a27b1d04f36b1c42e77a95f34d1a3a8370fd44738f2d2ba",
  "cid": "QmV10f97f5f62d9d277d8a27b1d04f36b1c42e77a95f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287616,
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
      "evaluated_at": 1760287616
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
  "sig": "2659780f9db393e8d11897fae75cfc40ec477a253b3f4a1977038224f64f33e8"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 31413162, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}